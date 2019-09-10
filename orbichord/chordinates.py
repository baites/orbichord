"""Implement tools to compute chordinates and distances in a given scale."""

from music21.chord import Chord
from music21.pitch import Pitch
from music21.scale import ConcreteScale


def scalarNormalOrder(chord: Chord, scale: ConcreteScale) -> list:
    """
    Provide chord normal order using a given scale steps

    Parameters:
    chrod (Chrod): Chord to stimate normal order
    scale (ConcreteScale): Scale use a metric
    Return:
    list: List with scalar normal order
    """
    # Chordinates
    chrodinates = []
    # Loop over pitches and extract scale
    for number in sorted(chord.normalOrder):
        chrodinates.append(
            scale.getScaleDegreeFromPitch(
                Pitch(number)
            )
        )
    return chrodinates
