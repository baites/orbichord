"""
Example of generator primitives.

This example generates the space of C chromatic chords identify
by their ordered pitch class string that are also triads.
"""

from orbichord.generator import Generator
from music21.scale import ChromaticScale

scale = ChromaticScale()

chord_generator = Generator(
    dimension=3,
    pitches=scale.getPitches('C','B'),
    identify=lambda chord: chord.orderedPitchClassesString
)

for chord in chord_generator.run():
    print(chord.pitchedCommonName)
