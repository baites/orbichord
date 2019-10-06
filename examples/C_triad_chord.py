"""
Example of generator primitives.

This example generates the space of C chords identify by
their ordered pitch class string that are also triads.
"""

from orbichord.generator import Generator
from orbichord.symbol import chordSymbolFigure
from music21.scale import MajorScale

scale = MajorScale('C')

chord_generator = Generator(
    pitches = scale.getPitches('C','B'),
    select = lambda chord: chord.isTriad()
)

for chord in chord_generator.run():
    chord.inversion(0)
    print('{} {} {} ({})'.format(
        chord,
        chord.orderedPitchClassesString,
        chord.pitchedCommonName,
        chordSymbolFigure(chord)
    ))
