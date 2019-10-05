"""Define a set of common chord identyfier."""

from copy import deepcopy
from music21.chord import Chord
from orbichord.symbol import chordSymbolFigure


def chordPitchClasses(chord : Chord) -> str:
    """Identify chords based on its pitch classes.

    Parameters
    ----------
        chord : Chord
            Chord to be identified.
    Return
    ------
        str
            A string with the pitch classes.
    """
    string = '<'
    for pitch in chord.pitches:
        string += pitch.pitchClass
    string += '>'
    return string


def chordPitchNames(chord : Chord) -> str:
    """Identify chords based on its pitch names.

    Parameters
    ----------
        chord : Chord
            Chord to be identified.
    Return
    ------
        str
            A string with the pitch names.
    """
    string = ''
    for pitch in chord.pitches:
        string += pitch.name
    return string
