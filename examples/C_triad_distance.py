
from music21.chord import Chord
from music21.scale import MajorScale
from numpy import inf
from numpy import linalg as la
from orbichord.chordinate import EfficientVoiceLeading

CMaj = Chord('C E G')
GMaj = Chord('G B D')

max_norm_vl = EfficientVoiceLeading(
    scale = MajorScale('C'),
    metric = lambda delta: la.norm(delta, inf)
)
taxicab_norm_vl = EfficientVoiceLeading(
    scale = MajorScale('C'),
    metric = lambda delta: la.norm(delta, 1)
)
euclidean_norm_vl = EfficientVoiceLeading(
    scale = MajorScale('C'),
    metric = lambda delta: la.norm(delta, 2)
)

vl, distance = max_norm_vl(CMaj, GMaj)
print('CMaj-GMaj maximum norm efficient voice leading:', vl)
print('CMaj-GMaj maximum norm distance:', distance)

vl, distance = taxicab_norm_vl(CMaj, GMaj)
print('CMaj-GMaj taxicab norm efficient voice leading:', vl)
print('CMaj-GMaj taxicab norm distance:', distance)

vl, distance = euclidean_norm_vl(CMaj, GMaj)
print('CMaj-GMaj euclidean norm efficient voice leading:', vl)
print('CMaj-GMaj euclidean norm distance:', distance)
