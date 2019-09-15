"""Implement tools to compute chordinates and distances in a given scale."""

import itertools
import math
from music21.chord import Chord
from music21.pitch import Pitch
from music21.scale import ConcreteScale
from numpy import array
from typing import Callable


def scalarPoint(
    chord: Chord,
    scale: ConcreteScale
) -> list:
    """Provide chord scalar point using a given scale steps

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


def mod(x, y, d):
    """Implement a modify module to provide
    shortest possible voice leading.
    """
    positive = (x - y) % d
    negative = (y - x) % d
    if positive > negative:
        return -negative
    return positive


def interscalarVector(
    chordA: Chord,
    chordB: Chord,
    scale: ConcreteScale
) -> list:
    """Compute the interscalar distance between two chords

    Parameters
    ----------
        chrodA : Chrod
            Voice leading start chord
        chrodA : Chrod
            Voice leading end chord
        scale : ConcreteScale
            Scale use a metric
    Return
    ------
        list
            Voice leading scalar steps
    """
    pointA = scalarPoint(chordA, scale)
    pointB = scalarPoint(chordB, scale)
    if len(pointA) != len(pointB):
        raise ValueError('Chords are not of the same dimension!')
    dimension = len(pointA)
    max_scale_degree = scale.getDegreeMaxUnique()
    delta = [0]*dimension
    for i in range(dimension):
        delta[i] = mod(pointB[i], pointA[i], max_scale_degree)
    return delta


def interscalarMatrix(
    chordA: Chord,
    chordB: Chord,
    scale: ConcreteScale
) -> list:
    """Compute the interscalar matrix between two chords

    Parameters
    ----------
        chrodA : Chrod
            Voice leading start chord
        chrodA : Chrod
            Voice leading end chord
        scale : ConcreteScale
            Scale use a metric
    Return
    ------
        list
            List of voice leading scalar steps
    """
    pointA = sorted(scalarPoint(chordA, scale))
    pointB = sorted(scalarPoint(chordB, scale))
    if len(pointA) != len(pointB):
        raise ValueError('Chords are not of the same dimension!')
    dimension = len(pointA)
    voice_leadings = []
    max_scale_degree = scale.getDegreeMaxUnique()
    while pointB[0] < max_scale_degree:
        tmp = pointB[0]
        pointB = pointB[1:] + [tmp + max_scale_degree]
        delta = [0]*dimension
        for i in range(dimension):
            delta[i] = mod(pointB[i], pointA[i], max_scale_degree)
        voice_leadings.append(delta)
    return voice_leadings


class VoiceLeading:
    """
    Compute efficient voice leading between two chords.

    Attributes
    ----------
    scale
    metric
    """

    def __init__(self,
        scale: ConcreteScale,
        metric: Callable[[list], float]
    ):
        """Create a efficient voice leading object

        Parameters
        ----------
            scale : ConcreteScale
                Scale use to define voice leading steps
            metric : Callable[[list], float]
                Metric function
        """
        self._scale = scale
        self._metric = metric

    @property
    def scale(self):
        """Returns voice leaging scale."""
        return self._scale

    @property
    def metric(self):
        """Returns voice leaging metric."""
        return self._metric

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
        delta = interscalarVector(chordA, chordB, self._scale)
        distance = self._metric(delta)
        return delta, distance


class EfficientVoiceLeading:
    """
    Compute efficient voice leading between two chords.

    Attributes
    ----------
    scale
    metric
    """

    def __init__(self,
        scale: ConcreteScale,
        metric: Callable[[list], float]
    ):
        """Create a efficient voice leading object

        Parameters
        ----------
            scale : ConcreteScale
                Scale use to define voice leading steps
            metric : Callable[[list], float]
                Metric function
        """
        self._scale = scale
        self._metric = metric

    @property
    def scale(self):
        """Returns voice leaging scale."""
        return self._scale

    @property
    def metric(self):
        """Returns voice leaging metric."""
        return self._metric

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
        matrix = interscalarMatrix(chordA, chordB, self._scale)
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
