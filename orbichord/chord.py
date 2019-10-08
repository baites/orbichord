"""Implement identified chords."""

from music21.chord import Chord
from typing import Callable


class IdentifiedChord(Chord):
    """Extend Chord to be a hashable object.

    The hash is contructed from a identity function that
    map a chord in to a string.

    Parameters
    ----------
        identify : Callable[[Chord], str], optional
            Funtion to indentify chords.
        notes :
            Argument pass to chord constructor.
        keywords :
            Argument pass to chord constructor.

    Attributes
    ----------
    indentify
    """

    def __init__(self,
        identify : Callable[[Chord], str] = \
            lambda chord: chord.orderedPitchClassesString,
        notes=None,
        **keywords
    ):
        """Constructor"""
        super().__init__(notes, **keywords)
        self._identify = identify

    def __hash__(self):
        """Return a has of the string."""
        return hash(self._identify(self))

    def __eq__(self, other):
        """Overload comparison based hashable implementation."""
        if not isinstance(other, IdentifiedChord):
            return False
        return hash(self) == hash(other)

    @property
    def identify(self):
        """Return identify function."""
        return self._identify

    @property
    def identity(self):
        """Return identity string."""
        return self._identify(self)
