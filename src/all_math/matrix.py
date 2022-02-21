"""
matrix.py

Autorius: Maksim Kulagin

Data: 2022-02-20
"""

from __future__ import annotations
from typing import Callable, Final, Generic, Iterable, TypeVar

from .vector import Vector

ValueT = TypeVar('ValueT')

class Matrix(Generic[ValueT]):
    size_i: Final[int]
    size_j: Final[int]
    _container: list[list[ValueT]] # Final

    def __init__(self, size_i: int, size_j: int, initializer: Callable[[Vector], ValueT]):
        """Inicializuoja matricą"""

        self.size_i = size_i
        self.size_j = size_j

        self._container = [[initializer(Vector(i, j)) for j in range(size_j)] for i in range(size_i)]

    def is_inside(self, vector: Vector) -> bool:
        """Tikrina, ar vektorius yra matricos ribose"""

        return vector.i >= 0 and vector.i < self.size_i and vector.j >= 0 and vector.j < self.size_j

    def set_at_vector(self, vector: Vector, value: ValueT) -> None:
        """Įrašo reikšmę į nurodytą poziciją"""

        self._container[vector.i][vector.j] = value

    def set_at(self, i: int, j: int, value: ValueT) -> None:
        """Įrašo reikšmę į nurodytą poziciją"""

        self._container[i][j] = value

    def get_at_vector(self, vector: Vector) -> ValueT:
        """Gražina reikšmė nurodytoje pozicijoje"""

        return self._container[vector.i][vector.j]

    def get_at(self, i: int, j: int) -> ValueT:
        """Gražina reikšmė nurodytoje pozicijoje"""

        return self._container[i][j]

    def __eq__(self, other: object) -> bool:
        """Tikrina ar matricos yra lygios"""

        if isinstance(other, Matrix):
            for vector in self.each_vector():
                if self.get_at_vector(vector) != other.get_at_vector(vector):
                    return False

            return True
        return False

    def __hash__(self) -> int:
        """Skaičiuoja matricos maišos (angl. hash) reikšmę"""

        return hash(str(self))

    def each_i_j(self) -> Iterable[tuple[int, int]]:
        """Iteruoja per matricos pozicijas, gražinant poziciją dviejų skaičių pavidalu"""

        for i in range(self.size_i):
            for j in range(self.size_j):
                yield(i, j)

    def each_vector(self) -> Iterable[Vector]:
        """Iteruoja per matricos pozicijas, gražinant poziciją vektoriaus pavidalu"""

        for i, j in self.each_i_j():
            yield(Vector(i, j))
