"""Create maps used by orbichord.identify module."""

from collections import OrderedDict
import music21.chord
from music21.scale import ChromaticScale
import music21.harmony as harmony
from orbichord.identify import chordPitchClasses

from pprint import pprint

chords = OrderedDict()

# Get chromatic scale
pitches = ChromaticScale().getPitches('C','B')

# Loop over all possible roots
for root in pitches:
    for add1 in range(13):
        for kind in harmony.CHORD_TYPES.keys():
            if kind in ('pedal', 'power'):
                continue
            ref = harmony.ChordSymbol(
                root = root,
                kind = kind
            )
            basses = [None] + list(ref.pitches)[1:]
            for bass in basses:
                chord = harmony.ChordSymbol(
                    root = root,
                    kind = kind,
                    bass = bass
                )
                if add1 > 0: chord.add(add1-1)
                key = chordPitchClasses(chord)
                if key in chords:
                    continue
                try:
                    value = harmony.chordSymbolFigureFromChord(chord)
                except:
                    continue
                if value == 'Chord Symbol Cannot Be Identified':
                    continue
                chords[key] = value

# Save in file
with open('maps.py', 'w') as file:
    pprint(
        chords,
        stream = file,
        indent = 4
    )
