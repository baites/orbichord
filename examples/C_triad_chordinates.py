"""Example triad scalar normal order o"""

from music21.chord import Chord
from music21.scale import MajorScale
from orbichord.chordinate import scalarPoint

scale = MajorScale('C')
chord = Chord('C E G')

normal_order = chord.normalOrder
scalar_point = scalarPoint(chord, scale)

print('Chord normal order is ', normal_order)
print('Chord C scalar normal order is ', scalar_point)
