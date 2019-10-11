"""Generate quotient space of n-pich classes."""

import copy
from itertools import combinations_with_replacement
from music21.chord import Chord
from typing import Callable, Iterable, Iterator
from orbichord.chord import IdentifiedChord
from orbichord.symbol import hasChordSymbolFigure


class Generator:
    """Generate the space of n-pitches chords.

    Generate the space of n-pitches chords. The list of pitches to be used in
    the generation needs to be provided when instantiating the generator.

    It is assumed that chords are musical objects which are at least invariant
    under scale pitch shifts (O). Any other invariance depends on how chord
    pitches are combined and how chords are identified.

    You can further restrict the generation of chords by passing a select
    function that restricts the type of chords yielded by the generator.

    By default, the generator will produce 3-pitched chords with the same
    invariances as a pitch-class ser:
        * scale pitch shifts (O),
        * pitch class permutation (P),
        * pitch class cardinality (C)
    Moreover, by default only chords with know symbols are selected to be
    generated.

    Parameters
    ----------
        pitches : list
            List of music21.pitch.Pitch.
        dimension : int, optional
            Dimension of the space.
        combinator : Callable[[Iterable, int], Iterator], optional
            Iterator function to generate all chord combinations.
        identify : Callable[Chord, str], optional
            Funtion to indentify chords.
        select : Callable[Chord, str], optional
            Function to select chords.

    Raises
    ------
        ValueError
            if the dimension is negative.

    References
    ----------
        * Tymoczko, Dmitri. “The geometry of musical chords.”
          Science 313.5783 (2006): 72-74.
        * Callender, Clifton, Ian Quinn, and Dmitri Tymoczko.
          “Generalized voice-leading spaces.” Science 320.5874 (2008): 346-348.
        * Dmitri Tymoczko, A Geometry of Music: Harmony and Counterpoint
          in the Extended Common Practice, Oxford University Press, 2011.

    Examples
    --------
    >>> from orbichord.generator import Generator
    >>> from orbichord.symbol import chordSymbolFigure
    >>> from music21.scale import MajorScale
    >>> scale = MajorScale('C')
    >>> chord_generator = Generator(
    ...     pitches = scale.getPitches('C','B'),
    ...     select = lambda chord: chord.isTriad()
    >>> )
    >>> for chord in chord_generator.run():
    ...     print('{} {} - {}'.format(
    ...     chord,
    ...     chord.orderedPitchClassesString,
    ...     chordSymbolFigure(chord, inversion=0)
    ... ))
    <music21.chord.Chord C0 E0 G0> <047> - C
    <music21.chord.Chord C0 E0 A0> <049> - Am
    <music21.chord.Chord C0 F0 A0> <059> - F
    <music21.chord.Chord D0 F0 A0> <259> - Dm
    <music21.chord.Chord D0 F0 B0> <25B> - Bdim
    <music21.chord.Chord D0 G0 B0> <27B> - G
    <music21.chord.Chord E0 G0 B0> <47B> - Em
    """

    def __init__(self,
        pitches: list,
        dimension: int = 3,
        combinator: Callable[[Iterable, int], Iterator] =\
            combinations_with_replacement,
        identify: Callable[[Chord], str] = \
            lambda chord: chord.orderedPitchClassesString,
        select: Callable[[Chord], bool] = hasChordSymbolFigure
    ):
        """Constructor."""
        # Sanity checks
        if dimension <= 0:
            raise ValueError('The dimension has to be larger than zero.')
        # Setting private values
        self._pitches = pitches
        self._dimension = dimension
        self._combinator = combinator
        self._identify = identify
        self._select = select

    @property
    def pitches(self):
        """Return the generator pitches."""
        return self._pitches

    @property
    def dimension(self):
        """Return the generator dimension."""
        return self._dimension

    @property
    def combinator(self):
        """Return the generator combinator."""
        return self._combinator

    @property
    def identify(self):
        """Return the function use to identify chords."""
        return self._identify

    @property
    def select(self):
        """Return function to select chords."""
        return self._select

    @staticmethod
    def _copy_fix_octaves(pitches):
        """Make chord octive consistent with their
        location within the chord."""
        octave = pitches[0].octave
        new_pitches = []
        for pitch in pitches:
            new_pitch = copy.deepcopy(pitch)
            new_pitch.octave -= octave
            new_pitches.append(new_pitch)
        pitches = new_pitches
        for index in range(1, len(pitches)):
            prev = pitches[index-1]
            curr = pitches[index]
            while prev > curr:
                curr.octave += 1
        return pitches

    def run(self) -> Iterator[Chord]:
        """Generate a sequence of chords.

        Yields
        ------
            Iterator[Chord]
                An iterator to the chords in the space.
        """
        # List of identified chords
        vetoed_chords = set()

        # Sample the chord space as combination with
        # replacement of the scale pitches.
        for ntuple in self._combinator(
            self._pitches, self._dimension
        ):
            # Generate the chord
            chord = IdentifiedChord(
                identify = self._identify,
                notes = self._copy_fix_octaves(ntuple)
            )
            # Veto identical chords
            if chord in vetoed_chords:
                continue
            vetoed_chords.add(chord)
            # select the chord?
            if self._select and not self._select(chord):
                continue
            yield chord
