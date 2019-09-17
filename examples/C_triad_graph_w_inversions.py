import itertools
from music21.harmony import chordSymbolFigureFromChord
from music21.scale import MajorScale
from numpy import inf
from numpy import linalg as la
from orbichord.chordinate import VoiceLeading
from orbichord.graph import createGraph, convertGraphToData
from orbichord.generator import Generator
import orbichord.identify as identify

def combinator(iterable, dimension):
    return itertools.product(iterable, repeat = dimension)

scale = MajorScale('C')

chord_generator = Generator(
    pitches = scale.getPitches('C','B'),
    combinator = combinator,
    identify = identify.chordPitchNames,
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
    string = ' {} ({}): '.format(
        chordSymbolFigureFromChord(nodes[index]),
        identify.chordPitchNames(nodes[index])
    )
    for nindex in range(len(adjacencies[index])):
        neighbor = adjacencies[index][nindex]
        weight = weights[index][nindex]
        string = string + ' {} ({}),'.format(
            chordSymbolFigureFromChord(nodes[neighbor]),
            identify.chordPitchNames(nodes[neighbor])
        )
    print(string[:-1])
