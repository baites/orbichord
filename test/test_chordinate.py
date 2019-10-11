
from music21.chord import Chord
from music21.scale import ChromaticScale, MinorScale, MajorScale
from numpy import inf
from numpy import linalg as la
from orbichord.chordinate import *

# Define global variables
chord = Chord('C E G')


def test_scalePoint():
    """Test scalePoint module method."""
    scale = ChromaticScale('C')
    scalar_point = scalePoint(chord, scale)
    assert scalar_point == [0, 4, 7]
    scale = MajorScale('C')
    scalar_point = scalePoint(chord, scale)
    assert scalar_point == [0, 2, 4]


def test_standardSimplex():
    """Test standardSimplex module method."""
    scale = ChromaticScale('C')
    standard_simplex = standardSimplex(chord, scale)
    assert standard_simplex == [11/12, 4/12, 3/12]
    standard_simplex = standardSimplex(chord, scale, False)
    assert standard_simplex == [11, 4, 3]
    scale = MajorScale('C')
    standard_simplex = standardSimplex(chord, scale)
    assert standard_simplex == [6/7, 2/7, 2/7]
    standard_simplex = standardSimplex(chord, scale, False)
    assert standard_simplex == [6, 2, 2]


def test_interscalarMatrix():
    """Test interscalarMatrix module method."""
    scale = MajorScale('C')
    ref_chord = Chord('F B D')
    delta = interscalarMatrix(chord, ref_chord, scale)
    assert delta == [[1, 1, 2], [3, -3, -3], [-1, -1, -1]]


def test_EfficientVoiceLeading():
    """Test EfficientVoiceLeading module class."""
    D_minor_scale = MinorScale('D')
    D_minor_scale = Chord(D_minor_scale.getPitches('D4', 'C5'))
    E_major_scale = MajorScale('E')
    E_major_scale = Chord(E_major_scale.getPitches('E4', 'D#5'))
    scale = ChromaticScale('C')
    voice_leading = EfficientVoiceLeading(
        scale = ChromaticScale('C'),
        metric = lambda delta: la.norm(delta, inf)
    )
    vl, dist = voice_leading(
        D_minor_scale,
        E_major_scale,
    )
    assert vl == [1, 1, 0, 1, 1, 0, 1]
    assert dist == 1.0
