
from music21.chord import Chord
from music21.scale import MinorScale, MajorScale, ChromaticScale
from numpy import inf
from numpy import linalg as la
from orbichord.chordinate import efficientVoiceLeading


from music21.pitch import Pitch

reference_scale = ChromaticScale('C')
D_minor_scale = MinorScale('D')
E_major_scale = MajorScale('E')

# Create a chord using D minor scale pitches
D_minor_scale = Chord(D_minor_scale.getPitches('D4', 'C5'))
print('D minor scale == ', D_minor_scale)
# <music21.chord.Chord D4 E4 F4 G4 A4 B-4 C5>

# Create a chord using C# minor scale pitches
E_major_scale = Chord(E_major_scale.getPitches('E4', 'D#5'))
print('E major scale == ', E_major_scale)
# <music21.chord.Chord C#4 D#4 E4 F#4 G#4 A4 B4>

# Compute efficient voice leading
vl, dist = efficientVoiceLeading(
    D_minor_scale,
    E_major_scale,
    reference_scale,
    lambda delta: la.norm(delta, inf)
)

# Print efficient voice leading
print(
    'voice leading = {}, distance = {}'.format(vl, dist)
)
# voice leading = [-1, -1, -1, -1, -1, -1, -1], distance = 1.0
