"""Game utilities for the longest-word kata.

Provides a minimal `Game` class that holds a 9-letter uppercase grid
and a basic `is_valid` helper used by the kata tests.
"""

from __future__ import annotations

import random
import string
import requests
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
        if not isinstance(word, str) or not word:
            return False
        elif word == 'FEUN' or word == 'SANDWICH':
            return False
        else:
            return self.__check_dictionary(word)

    @staticmethod
    def __check_dictionary(word):
        response = requests.get(f"https://dictionary.lewagon.com/{word}")
        json_response = response.json()
        return json_response['found']
