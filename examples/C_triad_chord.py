"""
Example of generator primitives.

This example generates the space of C chords identify by
their ordered pitch class string that are also triads.
"""

from orbichord.generator import Generator
from music21.scale import MajorScale

scale = MajorScale('C')

chord_generator = Generator(
    dimension=3,
    pitches=scale.getPitches('C','B'),
    identify=lambda chord: chord.orderedPitchClassesString,
    filter=lambda chord: chord.isTriad()
)

for chord in chord_generator.run():
    print(chord.pitchedCommonName)
