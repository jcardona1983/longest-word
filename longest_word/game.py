"""Game utilities for the longest-word kata.

Provides a minimal `Game` class that holds a 9-letter uppercase grid
and a basic `is_valid` helper used by the kata tests.
"""

from __future__ import annotations

import random
import string
from typing import List


class Game:
    """A simple game holding a 9-letter uppercase grid."""

    def __init__(self) -> None:
        """Create a random grid of 9 uppercase letters.

        The grid is stored as a list of single-character strings.
        """
        self.grid: List[str] = [random.choice(string.ascii_uppercase) for _ in range(9)]

    def is_valid(self, word: str) -> bool:
        """Return True if `word` can be made from the grid letters.

        This consumes letters from a copy of the grid and verifies every
        character in `word` (case-insensitive) exists and can be removed.
        """
        if not word:
            return False

        letters = self.grid.copy()  # Consume letters from the grid
        for letter in word.upper():
            if letter in letters:
                letters.remove(letter)
            else:
                return False

        return True
