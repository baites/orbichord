"""Map postonal chord names to symbols commonly found on lead sheets."""

from copy import deepcopy
from music21.chord import Chord
from orbichord.identify import chordSymbolIndex
from orbichord.maps import SYMBOL_INDEX_TO_FIGURE


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
            Return if symbol figure exist (named chord).
    """
    key = chordSymbolIndex(chord)
    return key in SYMBOL_INDEX_TO_FIGURE


def chordSymbolFigure(
        chord : Chord,
        inversion : int = None
    ) -> str:
    """Identify chords based chord symbol figure.

    This only applies to chords commonly found on lead sheets.

    Parameters
    ----------
        chord : Chord
            Chord to be identified.
        inversion : int
            Inversion index.

    Return
    ------
        str
            A string with with the chord symbol figure.
    """
    key = chordSymbolIndex(chord)
    if key not in SYMBOL_INDEX_TO_FIGURE:
        return chord.pitchClasses
    figure, inversions = SYMBOL_INDEX_TO_FIGURE[key]
    if inversion is None:
        return figure
    key = inversions[inversion]
    figure, _ = SYMBOL_INDEX_TO_FIGURE[key]
    return figure
