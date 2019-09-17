"""
Example of generator primitives.

This example generates the space of C chords identify by
their ordered pitch class string that are also triads.
"""

from orbichord.generator import IdentifiedChord

C = IdentifiedChord(
    identify = lambda chord: chord.orderedPitchClassesString,
    notes = 'C4 E4 G4'
)

print(C.pitchedCommonName)
print(C.identify(C))
print(hash(C))

C_evil_twin = IdentifiedChord(
    identify = lambda chord: chord.orderedPitchClassesString,
    notes = 'C4 G4 E5'
)

print(C_evil_twin.identify(C_evil_twin))
print('Is hash(C) == hash(C_evil_twin)?: ', hash(C) == hash(C_evil_twin))
print('Is C == C_evil_twin?: ', C == C_evil_twin)
