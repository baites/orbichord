
from music21.chord import Chord
from music21.scale import MajorScale
from numpy import inf
from numpy import linalg as la
from orbichord.chordinate import efficientVoiceLeading


scale = MajorScale('C')
CMaj = Chord('C E G')
GMaj = Chord('G B D')

vl, distance = efficientVoiceLeading(CMaj, GMaj, scale, lambda delta: la.norm(delta, inf))
print('CMaj-GMaj maximum norm efficient voice leading:', vl)
print('CMaj-GMaj maximum norm distance:', distance)

vl, distance = efficientVoiceLeading(CMaj, GMaj, scale, lambda delta: la.norm(delta, 1))
print('CMaj-GMaj taxicab norm efficient voice leading:', vl)
print('CMaj-GMaj taxicab norm distance:', distance)

vl, distance = efficientVoiceLeading(CMaj, GMaj, scale, lambda delta: la.norm(delta, 2))
print('CMaj-GMaj euclidean norm efficient voice leading:', vl)
print('CMaj-GMaj euclidean norm distance:', distance)
