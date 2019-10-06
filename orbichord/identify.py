"""Define a set of common chord identyfier."""

from copy import deepcopy
from music21.chord import Chord


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
    veto = set()
    for pitch in chord.pitches:
        pc = pitch.pitchClass
        if pc in veto:
            continue
        if pc == 10:
            string += 'A'
        elif pc == 11:
            string += 'B'
        else:
            string += str(pitch.pitchClass)
        veto.add(pc)
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
