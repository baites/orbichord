"""Standard chord figures."""

from orbichord.chord import IdentifiedChord
from orbichord.generator import IdentifiedChord
from orbichord.maps import ORDERED_PITCH_CLASS_TO_FIGURE


def hasFigure(chord : IdentifiedChord) -> bool:
    """Return true if the chird has figure.

    This only applies to standard chords traditionally from
    occidental harmony theory.

    Parameters
    ----------
        chord : Chord
            Chord to be identified.
    Return
    ------
        bool:
            A string with with the chord symbol.
    """
    return chord.identity in ORDERED_PITCH_CLASS_TO_FIGURE


def chordFigure(chord : IdentifiedChord) -> str:
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
    return ORDERED_PITCH_CLASS_TO_FIGURE[chord.identity]
