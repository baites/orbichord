
from music21.chord import Chord
from orbichord.identify import *


def test_chordPitchClasses():
    """Test chordPitchClasses orbichord.identity module method."""
    assert chordPitchClasses(Chord('C E G')) == '<047>'
    assert chordPitchClasses(Chord('E G C')) == '<470>'
    assert chordPitchClasses(Chord('G C E')) == '<704>'
    assert chordPitchClasses(Chord('B D# G')) == '<B37>'
    assert chordPitchClasses(Chord('D# G B')) == '<37B>'
    assert chordPitchClasses(Chord('G B D#')) == '<7B3>'


def test_chordPitchNames():
    """Test chordPitchNames orbichord.identity module method."""
    assert chordPitchNames(Chord('C E G')) == 'CEG'
    assert chordPitchNames(Chord('E G C')) == 'EGC'
    assert chordPitchNames(Chord('G C E')) == 'GCE'


def test_chordSymbolIndex():
    """Test chordSymbolIndex orbichord.identity module method."""
    assert chordSymbolIndex(Chord('C E G')) == '<047>'
    assert chordSymbolIndex(Chord('C G E')) == '<047>'
    assert chordSymbolIndex(Chord('E G C')) == '<407>'
    assert chordSymbolIndex(Chord('E C G')) == '<407>'
    assert chordSymbolIndex(Chord('G C E')) == '<704>'
    assert chordSymbolIndex(Chord('G E C')) == '<704>'
    assert chordSymbolIndex(Chord('B D# G')) == '<B37>'
    assert chordSymbolIndex(Chord('B G D#')) == '<B37>'
    assert chordSymbolIndex(Chord('D# G B')) == '<37B>'
    assert chordSymbolIndex(Chord('D# B G')) == '<37B>'
    assert chordSymbolIndex(Chord('G B D#')) == '<73B>'
    assert chordSymbolIndex(Chord('G D# B')) == '<73B>'
