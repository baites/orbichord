"""
Example of generator primitives.

This example generates the space of C tetrachords identify by
their ordered pitch class string that contain a triad.
"""

from orbichord.generator import Generator
from music21.scale import MajorScale

scale = MajorScale('C')

chord_generator = Generator(
    dimension=4,
    pitches=scale.getPitches('C','B'),
    identify=lambda chord: chord.orderedPitchClassesString
)

for chord in chord_generator.run():
    print(chord.pitchedCommonName)
