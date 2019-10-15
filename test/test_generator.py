from orbichord.generator import *
from orbichord.symbol import chordSymbolFigure
from music21.scale import MajorScale

reference_chords = {
    'Am',
    'Apedal',
    'Asus2',
    'BIt+6',
    'Bdim',
    'Bpedal',
    'C',
    'Cpedal',
    'Cpower',
    'CpoweraddA',
    'CpoweraddB',
    'Csus2',
    'Dm',
    'Dpedal',
    'Dpower',
    'DpoweraddB',
    'Dsus2',
    'Em',
    'Epedal',
    'Epower',
    'EpoweraddF',
    'F',
    'Fpedal',
    'Fsus2',
    'G',
    'Gpedal',
    'Gsus2'}


def test_common_Generator():
    """Test Generator module class."""
    scale = MajorScale('C')
    chord_generator = Generator(
        pitches = scale.getPitches('C','B')
    )
    generated_chords = set()
    for chord in chord_generator.run():
        generated_chords.add(
            chordSymbolFigure(chord, inversion=0)
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
