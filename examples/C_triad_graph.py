
from music21.harmony import chordSymbolFigureFromChord
from music21.scale import MajorScale
from numpy import inf
from numpy import linalg as la
from orbichord.chordinate import EfficientVoiceLeading
from orbichord.graph import createGraph, convertGraphToData
from orbichord.generator import Generator

scale = MajorScale('C')

chord_generator = Generator(
    dimension=3,
    pitches=scale.getPitches('C','B'),
    identify=lambda chord: chord.orderedPitchClassesString,
    select=lambda chord: chord.isTriad()
)

max_norm_vl = EfficientVoiceLeading(
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
    node.inversion(0)
    string =chordSymbolFigureFromChord(node) + ': '
    for nindex in range(len(adjacencies[index])):
        neighbor = adjacencies[index][nindex]
        strength = weights[index][nindex]
        nodes[neighbor].inversion(0)
        string = string + ' {} ({}),'.format(
            chordSymbolFigureFromChord(nodes[neighbor]), strength
        )
    print(string[:-1])
