import itertools
from music21.harmony import chordSymbolFigureFromChord
from music21.scale import MajorScale
from numpy import inf
from numpy import linalg as la
from orbichord.chordinate import VoiceLeading
from orbichord.graph import createGraph, convertGraphToData
from orbichord.generator import Generator

def combinator(iterable, dimension):
    return itertools.product(iterable, repeat = dimension)

scale = MajorScale('C')

chord_generator = Generator(
    pitches = scale.getPitches('C','B'),
    combinator = combinator,
    identify = chordSymbolFigureFromChord,
    select = lambda chord: chord.isTriad()
)

max_norm_vl = VoiceLeading(
    scale = scale,
    metric = lambda delta: la.norm(delta, inf)
)

nodes, adjacencies, weights = createGraph(
    generator = chord_generator,
    voice_leading = max_norm_vl,
    tolerance = lambda x: x <= 1.0
)

for index in range(len(nodes)):
    node = nodes[index]
    string = chordSymbolFigureFromChord(node) + ': '
    for nindex in range(len(adjacencies[index])):
        neighbor = adjacencies[index][nindex]
        strength = weights[index][nindex]
        string = string + ' {} ({}),'.format(
            chordSymbolFigureFromChord(nodes[neighbor]), strength
        )
    print(string[:-1])
