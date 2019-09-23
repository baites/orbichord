"""
Example of generator primitives.

This example generates the space of C chromatic chords identify
by their ordered pitch class string that are also triads.
"""

from orbichord.generator import Generator
from orbichord.identify import chordSymbolFigureNoInversion
from music21.scale import ChromaticScale

scale = ChromaticScale()

chord_generator = Generator(
    pitches = scale.getPitches('C','B'),
    select = None
)

for chord in chord_generator.run():
    print('{} {} {} ({})'.format(
        chord,
        chord.orderedPitchClassesString,
        chord.pitchedCommonName,
        chordSymbolFigureNoInversion(chord)
    ))
