
from music21.chord import Chord
from music21.scale import MajorScale
from orbichord.chordinate import interscalarMatrix

scale = MajorScale('C')
chordA = Chord('C E G')
chordB = Chord('F B D')
matrix = interscalarMatrix(chordA, chordB, scale)
print(matrix)
