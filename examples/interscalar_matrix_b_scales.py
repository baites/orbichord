
from music21.chord import Chord
from music21.scale import MajorScale, ChromaticScale
from numpy import inf
from numpy import linalg as la
from orbichord.chordinate import interscalarMatrix


scale = ChromaticScale('C')
chordA = Chord('C D E F G A B')
chordB = Chord('C D E F# G A B')
matrix = interscalarMatrix(chordA, chordB, scale)

print(matrix)
