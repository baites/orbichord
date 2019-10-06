from orbichord.generator import *
from orbichord.symbol import chordSymbolFigure
from music21.scale import MajorScale


def test_common_Generator():
    """Test Generator module class."""
    scale = MajorScale('C')
    chord_generator = Generator(
        pitches = scale.getPitches('C','B')
    )
    reference_chords = set((
        'Cpedal', 'Fpower', 'Cpower', 'Csus2', 'C',
        'Am', 'Csus', 'F', 'Dpedal', 'Gpower',
        'Dpower', 'Dsus2', 'Dm', 'Bdim', 'Dsus',
        'G', 'Epedal', 'Apower', 'Epower', 'Em',
        'Esus', 'Fpedal', 'BIt+6', 'Gpedal', 'Apedal','Bpedal',
    ))
    generated_chords = set()
    for chord in chord_generator.run():
        generated_chords.add(
            chordSymbolFigure(chord)
        )
    assert generated_chords <= reference_chords
    assert generated_chords >= reference_chords


def test_triad_Generator():
    """Test Generator module class."""
    scale = MajorScale('C')
    chord_generator = Generator(
        pitches = scale.getPitches('C','B'),
        select = lambda chord: chord.isTriad()
    )
    reference_chords = set((
        'C', 'Dm', 'Em', 'F', 'G', 'Am', 'Bdim'
    ))
    generated_chords = set()
    for chord in chord_generator.run():
        chord.inversion(0)
        generated_chords.add(
            chordSymbolFigure(chord)
        )
    assert generated_chords <= reference_chords
    assert generated_chords >= reference_chords
