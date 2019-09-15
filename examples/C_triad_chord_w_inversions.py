"""
Example of generator primitives.

This example generates the space of C chords identify by
their ordered pitch class string that are also triads.
"""

import itertools
from orbichord.generator import Generator
from music21.harmony import chordSymbolFigureFromChord
from music21.scale import MajorScale

def combinator(iterable, dimension):
    return itertools.product(iterable, repeat = dimension)

scale = MajorScale('C')

chord_generator = Generator(
    pitches = scale.getPitches('C','B'),
    combinator = combinator,
    identify = None,
    select = lambda chord: chord.isTriad()
)

for chord in chord_generator.run():
    print(
        chord,
        chord.orderedPitchClassesString,
        chord.pitchedCommonName,
        chordSymbolFigureFromChord(chord)
    )
