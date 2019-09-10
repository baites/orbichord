
from music21.chord import Chord
from music21.scale import MajorScale
from numpy import array, inf
from numpy import linalg as la
from orbichord.chordinates import scalarNormalOrder

scale = MajorScale('C')
CM = Chord('C E G')
GM = Chord('G B D')

CM_array = array(scalarNormalOrder(CM, scale))
GM_array = array(scalarNormalOrder(GM, scale))
delta = CM_array - GM_array

print(CM_array, GM_array)

print('CM-GM maximum norm distance:', la.norm(delta, inf))
