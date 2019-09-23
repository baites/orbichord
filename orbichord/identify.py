"""Define a set of common chord identyfier."""

from copy import deepcopy
from music21.chord import Chord
from music21.harmony import chordSymbolFigureFromChord


def chordSymbolFigureNoInversion(chord : Chord) -> str:
    """Identify chords based chord symbol figure.

    This only applies to standard chords traditionally from
    occidental harmony theory.

    Parameters
    ----------
        chord : Chord
            Chord to be identified.
    Return
    ------
        str
            A string with with the chord symbol.
    """
    temp = deepcopy(chord)
    temp.inversion(0)
    return chordSymbolFigureFromChord(temp)


def chordPitchNames(chord : Chord) -> str:
    """Identify chords based on its pitch names.

    Parameters
    ----------
        chord : Chord
            Chord to be identified.
    Return
    ------
        str
            A string with the pitch names in order.
    """
    string = ''
    for pitch in chord.pitches:
        string += pitch.name
    return string


def chordSymbolFigureWithPitchName(chord):
    """Identify chords based on its symbol and pitch names.

    This only applies to standard chords traditionally from
    occidental harmony theory.

    Parameters
    ----------
        chord : Chord
            Chord to be identified.
    Return
    ------
        str
            A string with the pitch names in order.
    """
    return '{} ({})'.format(
        chordSymbolFigureFromChord(chord),
        chordPitchNames(chord)
    )
