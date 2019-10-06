"""
Example of generator primitives.

This example generates the space of C tetrachords identify by
their ordered pitch class string that contain a triad.
"""

from orbichord.generator import Generator
from orbichord.symbol import chordSymbolFigure, hasChordSymbolFigure
from music21.scale import MajorScale

scale = MajorScale('C')

chord_generator = Generator(
    pitches = scale.getPitches('C','B'),
    dimension = 4,
    select = lambda chord: chord.containsTriad()
)

for chord in chord_generator.run():
    print('{} {} ({})'.format(
        chord,
        chord.orderedPitchClassesString,
        chordSymbolFigure(chord)
    ))