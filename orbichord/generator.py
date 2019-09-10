"""Generate quotient space of n-pich classes."""

import itertools
import typing
from music21.chord import Chord


class Generator:
    """TODO."""

    def __init__(self,
        pitches: list,
        dimension: int,
        filter: typing.Callable[[Chord], bool] = None,
        identify: typing.Callable[[Chord], str] = None
    ):
        """
        Initialize the generator (Constructor).

        Parameters:
        pitches (list): List of music21.pitch.Pitch
        dimension (int): Dimension of the space
        filter (Callable[Chord, str]): Function to filter chords
        identify (Callable[Chord, str]): Funtion to indentify chords
        """
        # Sanity checks
        if dimension <= 0:
            raise ValueError('The dimension has to be larger than zero.')
        # Setting private values
        self._pitches = pitches
        self._dimension = dimension
        self._identify = identify
        self._filter = filter

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
    def filter(self):
        """Return function to filter chords."""
        return self._filter

    def run(self) -> typing.Iterator[Chord]:
        """
        Generate a sequence of chords.

        Returns:
        typing.Iterator[Chord]: an iterator to the chords in the space
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
            # Filter the chord?
            if self._filter and not self._filter(chord):
                continue
            yield chord
