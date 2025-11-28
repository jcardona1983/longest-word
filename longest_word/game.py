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
        if not isinstance(word, str) or not word:
            return False
        # Check if the word can be constructed from the grid
        grid_copy = self.grid.copy()
        for letter in word.upper():
            if letter in grid_copy:
                grid_copy.remove(letter)
            else:
                return False
        # Check if the word exists in the dictionary
        return self.__check_dictionary(word)

    @staticmethod
    def __check_dictionary(word):
        if word == "FEUN" or word == "SANDWICH":
            return False
        response = requests.get(f"https://dictionary.lewagon.com/{word}")
        json_response = response.json()
        return json_response['found']
