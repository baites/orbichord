"""Map postonal chord names to symbols commonly found on lead sheets."""

from music21.chord import Chord
from orbichord.generator import IdentifiedChord
from orbichord.maps import ORDERED_PITCH_CLASSES_TO_FIGURE


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
    return chord.orderedPitchClassesString in ORDERED_PITCH_CLASSES_TO_FIGURE


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
    key = chord.orderedPitchClassesString
    return ORDERED_PITCH_CLASSES_TO_FIGURE[key]
