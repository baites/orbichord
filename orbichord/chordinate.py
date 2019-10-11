"""Implement tools to compute chordinates and distances in a given scale."""

from enum import Enum
import itertools
import math
from music21.chord import Chord
from music21.pitch import Pitch
from music21.scale import ConcreteScale
from numpy import array
from typing import Callable


def scalePoint(
    chord: Chord,
    scale: ConcreteScale
) -> list:
    """Compute chord coordinates using the degree for a given scale

    Parameters
    ----------
        chrod : Chrod
            Chord to estimate normal order
        scale : ConcreteScale
            Scale use as metric step

    Return
    ------
        list
            List with scalar normal order

    Examples
    --------
    >>> from music21.chord import Chord
    >>> from music21.scale import MajorScale
    >>> from orbichord.chordinate import scalePoint
    >>> scale = MajorScale('C')
    >>> chord = Chord('C E G')
    >>> scalePoint(chord, scale)
    [0, 2, 4]
    """
    # Chordinates
    point = []
    # Loop over pitches and extract scale
    for pitch in chord.pitches:
        point.append(
            scale.getScaleDegreeFromPitch(
                pitch, comparisonAttribute='pitchClass'
            ) - 1
        )
    return point


def standardSimplex(
    chord: Chord,
    scale: ConcreteScale,
    normalize: bool = True
) -> list:
    """Compute chord scale point in the standard simplex

    Parameters
    ----------
        chrod : Chrod
            Chord to estimate normal order
        scale : ConcreteScale
            Scale use as metric step
        normalize : int, optional
            Normalize coordinates by the number of scale degrees

    Return
    ------
        list
            List with scalar point within standard simplex

    Examples
    --------
    >>> from music21.chord import Chord
    >>> from music21.scale import ChromaticScale
    >>> from orbichord.chordinate import standardSimplex
    >>> scale = ChromaticScale('C')
    >>> chord = Chord('C E G')
    >>> standardSimplex(chord, scale)
    [0.9166666666666666, 0.3333333333333333, 0.25]
    >>> standardSimplex(chord, scale, normalize=False)
    [11, 4, 3]
    """
    # Get scale max degree and compute scalar point
    max_scale_degree = scale.getDegreeMaxUnique()
    point = scalePoint(chord, scale)
    # Reduce to the standard simplex
    dimension = len(point)
    sumchord = sum(point)
    point.sort()
    while sumchord >= max_scale_degree:
        last = point[-1]
        for index in range(1, dimension):
            point[dimension-index] = point[dimension-index-1]
        point[0] = last - max_scale_degree
        sumchord = sum(point)
    # Apply affine transformation
    previous = point[0]
    for index in range(1, dimension):
        interval = point[index] - previous
        previous = point[index]
        point[index] = interval
    point[0] = sumchord
    if normalize:
        for index in range(len(point)):
            point[index] /= max_scale_degree
    return point


def mod(x, y, d):
    """Implement a modify module to provide
    shortest possible voice leading.
    """
    positive = (x - y) % d
    negative = (y - x) % d
    if positive > negative:
        return -negative
    return positive


class Permutation(Enum):
    """Define type permutation used interscalar matrix."""
    NONE = 1
    CYCLIC = 2
    ANY = 3


def interscalarMatrix(
    chordA: Chord,
    chordB: Chord,
    scale: ConcreteScale,
    permutation: Permutation = Permutation.ANY
) -> list:
    """Compute the interscalar matrix between two chords

    Parameters
    ----------
        chrodA : Chrod
            Voice leading start chord.
        chrodA : Chrod
            Voice leading end chord
        scale : ConcreteScale
            Scale use a metric.
        permutation : Permutation, optional
            Permutation invariance in the interscalar matrix.

    Return
    ------
        list
            List of voice leading scalar steps

    Examples
    --------
    >>> from music21.chord import Chord
    >>> from music21.scale import MajorScale
    >>> from orbichord.chordinate import interscalarMatrix, Permutation
    >>> scale = MajorScale('C')
    >>> chordA = Chord('C E G')
    >>> chordB = Chord('A C E')
    >>> matrix = interscalarMatrix(
    ...     chordA, chordB, scale
    >>> )
    >>> print(matrix)
    [[0, 0, 1], [2, 3, 3], [-2, -2, -2]]
    """
    pointA = scalePoint(chordA, scale)
    pointB = scalePoint(chordB, scale)
    if len(pointA) != len(pointB):
        raise ValueError('Chords are not of the same dimension!')
    if permutation == Permutation.ANY:
        pointA.sort(); pointB.sort()
    dimension = len(pointA)
    voice_leadings = []
    max_scale_degree = scale.getDegreeMaxUnique()
    while pointB[0] < max_scale_degree:
        delta = [0]*dimension
        for i in range(dimension):
            delta[i] = mod(pointB[i], pointA[i], max_scale_degree)
        voice_leadings.append(delta)
        if permutation == Permutation.NONE:
            break
        tmp = pointB[0]
        pointB = pointB[1:] + [tmp + max_scale_degree]
    return voice_leadings


class EfficientVoiceLeading:
    """
    Compute efficient voice leading between two chords.

    Parameters
    ----------
        scale : ConcreteScale
            Scale use to define voice leading steps
        metric : Callable[[list], float]
            Metric function
        permutation : Permutation, optional
            Permutation invariance in the voice leading.

    Examples
    --------
    >>> from music21.chord import Chord
    >>> from music21.scale import MajorScale
    >>> from numpy import inf
    >>> from numpy import linalg as la
    >>> from orbichord.chordinate import EfficientVoiceLeading
    >>> scale = MajorScale('C')
    >>> C = Chord('C E G')
    >>> G = Chord('G B D')
    >>> voice_leading = EfficientVoiceLeading(
    ...     scale = scale,
    ...     metric = lambda delta: la.norm(delta, inf)
    >>> )
    >>> vl, dist = voice_leading(C, G)
    >>> print(vl, dist)
    [-1, -1, 0] 1.0
    """

    def __init__(self,
        scale: ConcreteScale,
        metric: Callable[[list], float],
        permutation: Permutation = Permutation.ANY
    ):
        """Constructor."""
        self._scale = scale
        self._metric = metric
        self._permutation = permutation

    @property
    def scale(self):
        """Returns voice leaging scale."""
        return self._scale

    @property
    def metric(self):
        """Returns voice leaging metric."""
        return self._metric

    @property
    def permutation(self):
        """Returns voice leaging metric."""
        return self._permutation

    def __call__(self,
        chordA: Chord,
        chordB: Chord,
    ) -> tuple:
        """Return the efficient voice leading and its distance

        Parameters
        ----------
            chrodA : Chrod
                Voice leading start chord
            chrodA : Chrod
                Voice leading end chord

        Return
        ------
            tuple
                Efficient voice leading scalar steps and its distance
        """
        voice_leading_distance = None
        voice_leading_index = None
        matrix = interscalarMatrix(
            chordA, chordB, self._scale, self._permutation
        )
        for index in range(len(matrix)):
            voice_leading = matrix[index]
            distance = self._metric(voice_leading)
            if voice_leading_distance is None:
                voice_leading_distance = distance
                voice_leading_index = index
                continue
            if distance < voice_leading_distance:
                voice_leading_distance = distance
                voice_leading_index = index
        return matrix[voice_leading_index], voice_leading_distance
