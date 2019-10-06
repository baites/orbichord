"""Map postonal chord names to symbols commonly found on lead sheets."""

from music21.chord import Chord
from orbichord.identify import chordPitchClasses
from orbichord.maps import PITCH_CLASSES_TO_SYMBOL


def hasChordSymbolFigure(chord : Chord) -> bool:
    """Return true if the chord has figure.

    This only applies to chords commonly found on lead sheets.

    Parameters
    ----------
        chord : Chord
            Chord to be identified.
    Return
    ------
        bool:
            A string with with the chord symbol.
    """
    key = chordPitchClasses(chord)
    return key in PITCH_CLASSES_TO_SYMBOL


def chordSymbolFigure(chord : Chord) -> str:
    """Identify chords based chord symbol figure.

    This only applies to chords commonly found on lead sheets.

    Parameters
    ----------
        chord : Chord
            Chord to be identified.
    Return
    ------
        str
            A string with with the chord symbol.
    """
    key = chordPitchClasses(chord)
    return PITCH_CLASSES_TO_SYMBOL[key]
