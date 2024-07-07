from typing import Tuple


# A generic object to represent players, enemies, items, etc.
class Entity:
    def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int]):
        self.x = x
        self.y = y
        self.char = char
        self.color = color #Tuple rgb

    # Move the entity by a given amount
    def move(self, dx: int, dy: int) -> None:
        self.x += dx
        self.y += dy
