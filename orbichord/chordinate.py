"""Implement tools to compute chordinates and distances in a given scale."""

import itertools
from music21.chord import Chord
from music21.pitch import Pitch
from music21.scale import ConcreteScale
from numpy import array


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
            scale.getScaleDegreeFromPitch(pitch)-1
        )
    return point


def scalarDistance(
    chordA: Chord,
    chordB: Chord,
    scale: ConcreteScale,
    metric
) -> float:
    """TODO."""
    distances = []
    pointB = array(scalarPoint(chordB, scale))
    for perm in itertools.permutations(chordA.pitches):
        pointA = array(scalarPoint(Chord(perm), scale))
        delta = (pointA - pointB) % scale.getDegreeMaxUnique()
        distances.append(metric(delta))
    return min(distances)
