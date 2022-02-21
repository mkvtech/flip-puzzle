"""
vector.py

Autorius: Maksim Kulagin

Data: 2022-02-20
"""

from __future__ import annotations
from typing import Final

class Vector:
    """Objektas, kuris saugo dvi reikšmės"""

    i: Final[int]
    j: Final[int]

    def __init__(self, i: int, j: int):
        """Initializuoja vectorių"""

        self.i = i
        self.j = j

    def up(self, count: int = -1) -> Vector:
        """Gražina vektorių, kuris yra viršuje"""

        return Vector(self.i + count, self.j)

    def down(self, count: int = 1) -> Vector:
        """Gražina vektorių, kuris yra apačioje"""

        return Vector(self.i + count, self.j)

    def right(self, count: int = 1) -> Vector:
        """Gražina vektorių, kuris yra dešinėje"""

        return Vector(self.i, self.j + count)

    def left(self, count: int = -1) -> Vector:
        """Gražina vektorių, kuris yra kairėje"""

        return Vector(self.i, self.j + count)

    def neighbours(self) -> list[Vector]:
        """Gražina keturių vektorių sąrašą"""

        return [self.up(), self.down(), self.right(), self.left()]

    def __str__(self) -> str:
        """Gražina vektoriaus 'string' formą"""

        return f'({self.i}, {self.j})'

    def __eq__(self, other: object) -> bool:
        """Tikrina, ar du vektoriai yra lygus"""

        return isinstance(other, Vector) and self.i == other.i and self.j == other.j

    def __hash__(self) -> int:
        """Skaičiuoja matricos maišos (angl. hash) reikšmę"""

        return hash((self.i, self.j))
