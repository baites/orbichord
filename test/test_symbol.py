from music21.chord import Chord
from music21.harmony import ChordSymbol
from orbichord.symbol import *


def test_hasChordSymbolFigure():
    """Test hasChordSymbolFigure orbichord.symbol module method."""

    # Basic asserts
    assert hasChordSymbolFigure(Chord('C E G')) == True
    assert hasChordSymbolFigure(Chord('C C G')) == True

    # Checking chord symbols
    chord = ChordSymbol(root='C', bass='G#', kind='augmented')
    assert hasChordSymbolFigure(chord) == True

    chord = ChordSymbol(root='C', bass='G#', kind='augmented')
    chord.add('C#')
    assert hasChordSymbolFigure(chord) == True


def test_chordSymbolFigure():
    """Test chordSymbolFigure orbichord.symbol module method."""

    # Normal chords
    chord = Chord('C E G')
    assert chordSymbolFigure(chord) == 'C'
    assert chordSymbolFigure(chord, inversion=0) == 'C'
    assert chordSymbolFigure(chord, inversion=1) == 'C/E'
    assert chordSymbolFigure(chord, inversion=2) == 'C/G'

    chord = Chord('B D# F#')
    assert chordSymbolFigure(chord) == 'B'
    assert chordSymbolFigure(chord, inversion=0) == 'B'
    assert chordSymbolFigure(chord, inversion=1) == 'B/D#'
    assert chordSymbolFigure(chord, inversion=2) == 'B/F#'

    # Good twin inversion
    chord = Chord('G C E')
    assert chordSymbolFigure(chord) == 'C/G'
    assert chordSymbolFigure(chord, inversion=0) == 'C'
    chord = Chord('F# B D#')
    assert chordSymbolFigure(chord) == 'B/F#'
    assert chordSymbolFigure(chord, inversion=0) == 'B'

    # Evil twin inversion
    chord = Chord('G E C')
    assert chordSymbolFigure(chord) == 'C/G'
    assert chordSymbolFigure(chord, inversion=0) == 'C'
    chord = Chord('F# D# B')
    assert chordSymbolFigure(chord) == 'B/F#'
    assert chordSymbolFigure(chord, inversion=0) == 'B'
