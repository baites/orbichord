"""Create maps used by orbichord.identify module."""

from collections import OrderedDict
from music21.scale import ChromaticScale
import music21.harmony as harmony
from pprint import pprint

ORDERED_PITCH_CLASS_TO_FIGURE = OrderedDict()

# Get chromatic scale
pitches = ChromaticScale().getPitches('C', 'B')

# Loop over all possible roots
for root in pitches:
    # Loop over all possible types
    for kind in harmony.CHORD_TYPES.keys():
        chord = harmony.ChordSymbol(
            root = root,
            kind = kind
        )
        key = chord.orderedPitchClassesString
        value = chord.figure
        if key in ORDERED_PITCH_CLASS_TO_FIGURE:
            continue
        ORDERED_PITCH_CLASS_TO_FIGURE[key] = value

# Save in file
with open('maps.py', 'w') as file:
    pprint(
        ORDERED_PITCH_CLASS_TO_FIGURE,
        stream = file,
        indent = 4
    )
