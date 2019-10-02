
from music21.chord import Chord
from music21.scale import ChromaticScale, MajorScale
from orbichord.chordinate import *

# Define global variables
chord = Chord('C E G')


def test_scalarPoint():
    """Test scalarPoint module method."""
    scale = ChromaticScale('C')
    scalar_point = scalarPoint(chord, scale)
    assert scalar_point == [0, 4, 7]
    scale = MajorScale('C')
    scalar_point = scalarPoint(chord, scale)
    assert scalar_point == [0, 2, 4]


def test_standardSimplex():
    """Test standardSimplex module method."""
    scale = ChromaticScale('C')
    standard_simplex = standardSimplex(chord, scale)
    assert standard_simplex == [11/12, 4/12, 3/12]
    scale = MajorScale('C')
    standard_simplex = standardSimplex(chord, scale)
    assert standard_simplex == [6/7, 2/7, 2/7]


def test_interscalarVector():
    """Test interscalarVector module method."""
    scale = MajorScale('C')
    ref_chord = Chord('F B D')
    delta = interscalarVector(chord, ref_chord, scale)
    assert delta == [3, -3, -3]


def test_interscalarMatrix():
    """Test interscalarMatrix module method."""
    scale = MajorScale('C')
    ref_chord = Chord('F B D')
    delta = interscalarMatrix(chord, ref_chord, scale)
    assert delta == [[1, 1, 2], [3, -3, -3], [-1, -1, -1]]
