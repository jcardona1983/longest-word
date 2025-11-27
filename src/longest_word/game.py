import random
import string
from typing import List


class Game:
    def __init__(self) -> None:
        """Attribute a random grid of size 9 (list of uppercase letters)."""
        self.grid: List[str] = [random.choice(string.ascii_uppercase) for _ in range(9)]

    def is_valid(self, word: str) -> bool:
        """Placeholder implementation for kata completeness."""
        if not isinstance(word, str) or not word:
            return False
        return True


__all__ = ["Game"]
