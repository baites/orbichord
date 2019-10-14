"""Define a set of common chord identyfier."""

from copy import deepcopy
from music21.chord import Chord
from typing import Callable


def base10toN(num: int, base: int=12):
    """Change to given base upto base 36 is supported.

    Parameters
    ----------
        num : int
            Integer to be transform to new base.
        base : int
            Based to use write the integer.

    Return
    ------
        str
            String with number digits in new base.

    References
    ----------
        * http://code.activestate.com/recipes/577586-converts-from-decimal-to-any-base-between-2-and-26/
    """
    converted_string = ""
    currentnum = num
    if not 1 < base < 37:
        raise ValueError("base must be between 2 and 36")
    if not num:
        return '0'
    while currentnum:
        mod = currentnum % base
        currentnum = currentnum // base
        converted_string = chr(48 + mod + 7*(mod >= 10)) + converted_string
    return converted_string


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
    pcs = chord.pitchClasses
    return '<' + ''.join(map(base10toN, pcs)) + '>'


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
    names = map(
        lambda pitch: pitch.name,
        chord.pitches
    )
    return ''.join(names)


def chordSymbolIndex(chord : Chord) -> str:
    """Identify chords based on its chord symbol index.

    The chord symbol index is an index that is unique to each named chord.

    Parameters
    ----------
        chord : Chord
            Chord to be identified.

    Return
    ------
        str
            A string with the pitch names.
    """
    # Remove repeated pitch class
    pcs = []
    veto = set()
    for pc in chord.pitchClasses:
        if pc in veto:
            continue
        pcs.append(pc)
        veto.add(pc)
    # The first pc is the bass, the remaining ps
    # are sorted to treat each inversion the same
    # independent of the permutations.
    pcs = [pcs[0]] + sorted(pcs[1:])
    return '<' + ''.join(map(base10toN, pcs)) + '>'
