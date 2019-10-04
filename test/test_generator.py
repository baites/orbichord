from orbichord.generator import *
from orbichord.identify import chordSymbolFigureNoInversion
from music21.scale import MajorScale

def test_Generator():
    """Test Generator module class."""
    scale = MajorScale('C')
    chord_generator = Generator(
        pitches = scale.getPitches('C','B'),
    )
    reference_chords = set((
        'C', 'Dm', 'Em', 'F', 'G', 'Am', 'Bdim'
    ))
    generated_chords = set()
    for chord in chord_generator.run():
        generated_chords.add(
            chordSymbolFigureNoInversion(chord)
        )
    assert generated_chords <= reference_chords
    assert generated_chords >= reference_chords
