
from music21.scale import MajorScale
from numpy import inf
from numpy import linalg as la
from orbichord.chordinate import EfficientVoiceLeading
from orbichord.graph import createGraph, convertGraphToData
from orbichord.generator import Generator
from orbichord.symbol import chordSymbolFigure


graph_string = """C:  Am (1.0), F (1.0), Dm (1.0), Bdim (1.0), G (1.0), Em (1.0)
Am:  C (1.0), F (1.0), Dm (1.0), Bdim (1.0), G (1.0), Em (1.0)
F:  C (1.0), Am (1.0), Dm (1.0), Bdim (1.0), G (1.0), Em (1.0)
Dm:  C (1.0), Am (1.0), F (1.0), Bdim (1.0), G (1.0), Em (1.0)
Bdim:  C (1.0), Am (1.0), F (1.0), Dm (1.0), G (1.0), Em (1.0)
G:  C (1.0), Am (1.0), F (1.0), Dm (1.0), Bdim (1.0), Em (1.0)
Em:  C (1.0), Am (1.0), F (1.0), Dm (1.0), Bdim (1.0), G (1.0)"""


def test_createGraph():
    """Test createGraph module member."""

    scale = MajorScale('C')

    chord_generator = Generator(
        pitches = scale.getPitches('C','B'),
        select = lambda chord: chord.isTriad()
    )

    max_norm_vl = EfficientVoiceLeading(
        scale = scale,
        metric = lambda delta: la.norm(delta, inf)
    )

    graph, _ = createGraph(
        generator = chord_generator,
        voice_leading = max_norm_vl,
        tolerance = lambda x: x == 1.0,
        label = lambda chord: chordSymbolFigure(chord, inversion=0)
    )

    string = ''
    for node, neighbors in graph.adjacency():
        line = node + ': '
        for neighbor, edge in neighbors.items():
            line += ' {} ({}),'.format(
                neighbor, edge['distance']
            )
        string += line[:-1] + '\n'
    assert string[:-1] == graph_string
