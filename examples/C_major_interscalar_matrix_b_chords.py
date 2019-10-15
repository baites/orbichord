
from music21.chord import Chord
from music21.scale import MajorScale, ChromaticScale
from orbichord.chordinate import interscalarMatrix, Permutation

scale = MajorScale('C')

# Chords are good twins

chordA = Chord('C E G')
chordB = Chord('A C E')

# Interscalar assuming any permutation
matrix = interscalarMatrix(
    chordA, chordB, scale
)
print(matrix)
# Interscalar assuming cyclic permutation
matrix = interscalarMatrix(
    chordA, chordB, scale, permutation = Permutation.CYCLIC
)
print(matrix)
# Interscalar assuming no permutation
matrix = interscalarMatrix(
    chordA, chordB, scale, permutation = Permutation.NONE
)
print(matrix)

# First ans second chord is good and bad twin, respectively.

chordA = Chord('C E G')
chordB = Chord('A E C')

# Interscalar assuming any permutation
matrix = interscalarMatrix(
    chordA, chordB, scale
)
print(matrix)
# Interscalar assuming cyclic permutation
matrix = interscalarMatrix(
    chordA, chordB, scale, permutation = Permutation.CYCLIC
)
print(matrix)
# Interscalar assuming no permutation
matrix = interscalarMatrix(
    chordA, chordB, scale, permutation = Permutation.NONE
)
print(matrix)

# Chords with duplicated pitches
scale = ChromaticScale('C')

chordA = Chord('E- A- C  C')
chordB = Chord('E  E  A- B')

# Interscalar assuming any permutation
matrix = interscalarMatrix(
    chordA, chordB, scale
)
print(matrix)

# Interscalar without cardinality invariance
matrix = interscalarMatrix(
    chordA, chordB, scale, cardinality = False
)
print(matrix)
