
from music21.chord import Chord
from music21.scale import MajorScale
from numpy import inf
from numpy import linalg as la
from orbichord.chordinate import scalarDistance


scale = MajorScale('C')
CM = Chord('C E G')
GM = Chord('G B D')

distance = scalarDistance(CM, GM, scale, lambda delta: la.norm(delta, inf))
print('CM-GM maximum norm distance:', distance)

distance = scalarDistance(CM, GM, scale, lambda delta: la.norm(delta, 1))
print('CM-GM taxicab norm distance:', distance)

distance = scalarDistance(CM, GM, scale, lambda delta: la.norm(delta, 2))
print('CM-GM euclidean norm distance:', distance)
