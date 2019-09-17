"""Define a set of common chord identyfier."""

from music21.chord import Chord

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
