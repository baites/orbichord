"""Generate quotient space of n-pich classes."""

import copy
from itertools import combinations_with_replacement
from music21.chord import Chord
from typing import Callable, Iterable, Iterator
from orbichord.chord import IdentifiedChord
import orbichord.identify as identify
from orbichord.symbol import hasFigure


class Generator:
    """Generate the space of n-pitches chords.

    Generate the space of n-pitches chords. The list of pitches to be used in
    the generation needs to be provided when instantiating the generator.

    It is assumed that chords are musical objects which are at least invariant
    under
        * scale pitch shifts (O),
        * pitch permutation (P),
        * pitch cardinality or dimension (C)

    By default chords with repeated pitches are not identified as the same
    chord. If you wish to do so, you can pass an identitying function that
    provides a hashable object to classify different objects as the same chord.
    On the first object of the identification will be yield by the generator.

    You can further restrict the generation of chords by passing a select
    function that restricts the type of chords yielded by the generator.

    Attributes
    ----------
    pitches
    dimension
    combinator
    identity
    select
    """

    def __init__(self,
        pitches: list,
        dimension: int = 3,
        combinator: Callable[[Iterable, int], Iterator] =\
            combinations_with_replacement,
        identify: Callable[[Chord], str] = \
            lambda chord: chord.orderedPitchClassesString,
        select: Callable[[Chord], bool] = hasFigure
    ):
        """Initialize the generator (Constructor).

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
        Raises:
        -------
            ValueError
                if the dimension is negative.
        """
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
