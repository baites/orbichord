"""
Example of generator primitives.

This example generates the space of C trichords identify by
their ordered pitch class string.
"""

from orbichord.generator import Generator
from music21.scale import MajorScale

scale = MajorScale('C')

chord_generator = Generator(
    pitches=scale.getPitches('C','B'),
    select=None
)

for chord in chord_generator.run():
    print(
        chord,
        chord.orderedPitchClassesString,
        chord.pitchedCommonName
    )
