"""Create maps used by orbichord.identify module."""

from collections import OrderedDict
import music21.chord
from music21.scale import ChromaticScale
import music21.harmony as harmony
from orbichord.identify import chordSymbolIndex

from pprint import pprint

chords = OrderedDict()

# Get chromatic scale
pitches = ChromaticScale().getPitches('C','B')

# Loop over all possible roots
for add1 in range(13):
    for kind in harmony.CHORD_TYPES.keys():
        for root in pitches:
            ref = harmony.ChordSymbol(
                root = root,
                kind = kind
            )
            basses = [None] + list(ref.pitches)[1:]
            inversions = []
            for bass in basses:
                chord = harmony.ChordSymbol(
                    root = root,
                    kind = kind,
                    bass = bass
                )
                if add1 > 0: chord.add(add1-1)
                key = chordSymbolIndex(chord)
                if key in chords:
                    continue
                try:
                    value = harmony.chordSymbolFigureFromChord(chord)
                except:
                    continue
                if value == 'Chord Symbol Cannot Be Identified':
                    continue
                inversions.append(key)
                chords[key] = value
            for key in inversions:
                chords[key] = (chords[key], inversions)

# Save in file
with open('maps.py', 'w') as file:
    pprint(
        chords,
        stream = file,
        width = 300,
        indent = 4
    )
