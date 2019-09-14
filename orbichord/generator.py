"""Generate quotient space of n-pich classes."""

import itertools
import typing
from music21.chord import Chord


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
    identity
    select
    """

    def __init__(self,
        pitches: list,
        dimension: int,
        identify: typing.Callable[[Chord], str] = None,
        select: typing.Callable[[Chord], bool] = None
    ):
        """Initialize the generator (Constructor).

        Parameters
        ----------
            pitches : list
                List of music21.pitch.Pitch.
            dimension : int
                Dimension of the space.
            identify : Callable[Chord, str]
                Funtion to indentify chords.
            select : Callable[Chord, str]
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
        self._identify = identify
        self._select = select

    @property
    def pitches(self):
        """Return the generator pitches."""
        return self._pitches

    @property
    def dimension(self):
        """Return the the generator dimension."""
        return self._dimension

    @property
    def identify(self):
        """Return the function use to identify chords."""
        return self._identify

    @property
    def select(self):
        """Return function to select chords."""
        return self._select

    def run(self) -> typing.Iterator[Chord]:
        """Generate a sequence of chords.

        Yields
        ------
            typing.Iterator[Chord]
                An iterator to the chords in the space.
        """
        # List of identified chords
        identitied_chords = set()

        # Sample the chord space as combination with
        # replacement of the scale pitches.
        for ntuple in itertools.combinations_with_replacement(
            self._pitches, self._dimension
        ):
            # Generate the chord
            chord = Chord(ntuple)
            # Identify the chord
            if self._identify:
                identity = self._identify(chord)
                if identity in identitied_chords:
                    continue
                identitied_chords.add(identity)
            # select the chord?
            if self._select and not self._select(chord):
                continue
            yield chord
