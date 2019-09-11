"""Implement tools to compute chordinates and distances in a given scale."""

import itertools
import math
from music21.chord import Chord
from music21.pitch import Pitch
from music21.scale import ConcreteScale
from numpy import array
import typing


def scalarPoint(chord: Chord, scale: ConcreteScale) -> list:
    """
    Provide chord scalar point using a given scale steps

    Parameters:
    chrod (Chrod): Chord to stimate normal order
    scale (ConcreteScale): Scale use a metric
    Return:
    list: List with scalar normal order
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
    return sorted(point)


def mod(x, y, d):
    """
    Implement a modify module to provide
    shortest possible voice leading.
    """
    positive = (x - y) % d
    negative = (y - x) % d
    if positive > negative:
        return -negative
    return positive


def interscalarMatrix(
    chordA: Chord,
    chordB: Chord,
    scale: ConcreteScale
) -> list:
    """
    Compute the interscalar matrix between two chords

    Parameters:
    chrodA (Chrod): Voice leading start chord
    chrodA (Chrod): Voice leading end chord
    scale (ConcreteScale): Scale use a metric
    Return:
    list: List of voice leading scalar steps
    """
    pointA = scalarPoint(chordA, scale)
    pointB = scalarPoint(chordB, scale)
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


def efficientVoiceLeading(
    chordA: Chord,
    chordB: Chord,
    scale: ConcreteScale,
    metric: typing.Callable[[list], float]
) -> tuple:
    """
    Compute efficient voice leading for a given scale and metric

    Parameters:
    chrodA (Chrod): Voice leading start chord
    chrodA (Chrod): Voice leading end chord
    scale (ConcreteScale): Scale use a metric
    metric typing.Callable[[list], float]: Metric function
    Return:
    tuple: Efficient voice leading scalar steps and its distance
    """
    voice_leading_distance = None
    voice_leading_index = None
    matrix = interscalarMatrix(chordA, chordB, scale)
    for index in range(len(matrix)):
        voice_leading = matrix[index]
        distance = metric(voice_leading)
        if voice_leading_distance is None:
            voice_leading_distance = distance
            voice_leading_index = index
            continue
        if distance < voice_leading_distance:
            voice_leading_distance = distance
            voice_leading_index = index
    return matrix[voice_leading_index], voice_leading_distance
