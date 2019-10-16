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
                bass = bass.name if bass else None
                chord = harmony.ChordSymbol(
                    root = root,
                    kind = kind,
                    bass = bass
                )
                if add1 > 0: chord.add(add1-1)
                key = chordSymbolIndex(chord)
                try:
                    name = harmony.chordSymbolFigureFromChord(chord)
                except:
                    continue
                if name == 'Chord Symbol Cannot Be Identified':
                    continue
                if key not in chords:
                    inversions.append(key)
                names, _ = chords.setdefault(key, [[], None])
                if name in names:
                    continue
                names.append(name)
            for key in inversions:
                chords[key][1] = inversions

# Save in file
with open('maps.py', 'w') as file:
    pprint(
        chords,
        stream = file,
        width = 300,
        indent = 4
    )
