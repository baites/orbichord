"""Example triad scalar normal order o"""

from music21.chord import Chord
from music21.scale import MajorScale
from orbichord.chordinates import scalarNormalOrder

scale = MajorScale('C')
chord = Chord('C E G')
#chord = Chord('G B D')
print(chord.pitchedCommonName)

normalOrder = chord.normalOrder
scalarNormalOrder = scalarNormalOrder(chord, scale)

print('Chord normal order is ', normalOrder)
print('Chord C scalar normal order is ', scalarNormalOrder)
