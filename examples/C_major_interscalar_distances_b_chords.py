
from music21.chord import Chord
from music21.scale import MajorScale
from orbichord.chordinate import interscalarVector

scale = MajorScale('C')
chordA = Chord('C E G')
chordB = Chord('F B D ')
delta = interscalarVector(chordA, chordB, scale)
print(delta)
