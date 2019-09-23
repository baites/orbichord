"""Example of voice leading between scales."""

from music21.chord import Chord
from music21.pitch import Pitch
from music21.scale import MinorScale, MajorScale, ChromaticScale
from numpy import inf
from numpy import linalg as la
from orbichord.chordinate import EfficientVoiceLeading, interscalarMatrix

D_minor_scale = MinorScale('D')
E_major_scale = MajorScale('E')

# Create a chord using D minor scale pitches
D_minor_scale = Chord(D_minor_scale.getPitches('D4', 'C5'))
print('D minor scale == ', D_minor_scale)
# D minor scale == <music21.chord.Chord D4 E4 F4 G4 A4 B-4 C5>

# Create a chord using C# minor scale pitches
E_major_scale = Chord(E_major_scale.getPitches('E4', 'D#5'))
print('E major scale == ', E_major_scale)
# E major scale == <music21.chord.Chord E4 F#4 G#4 A4 B4 C#5 D#5>

voice_leading = EfficientVoiceLeading(
    scale = ChromaticScale('C'),
    metric = lambda delta: la.norm(delta, inf)
)

# Compute efficient voice leading
vl, dist = voice_leading(
    D_minor_scale,
    E_major_scale,
)

# Print efficient voice leading
print(
    'voice leading = {}, distance = {}'.format(vl, dist)
)
# voice leading = [1, 1, 0, 1, 1, 0, 1], distance = 1.0

# All possible voice leadings
print()
print('all possible voice leadings:')
matrix = interscalarMatrix(D_minor_scale, E_major_scale, ChromaticScale('C'))
for vl in matrix:
    print(
        'voice leading = {}, distance = {}'.format(vl, la.norm(vl, inf))
    )

# all possible voice leadings:
# voice leading = [1, 1, 0, 1, 1, 0, 1], distance = 1.0
# voice leading = [3, 2, 2, 3, 2, 2, 3], distance = 3.0
# voice leading = [4, 4, 4, 4, 4, 4, 5], distance = 5.0
# voice leading = [6, 6, 5, 6, 6, 6, 6], distance = 6.0
# voice leading = [-4, -5, -5, -4, -4, -5, -4], distance = 5.0
# voice leading = [-3, -3, -3, -2, -3, -3, -2], distance = 3.0
# voice leading = [-1, -1, -1, -1, -1, -1, -1], distance = 1.0
