"""
bool_matrix.py

Autorius: Maksim Kulagin

Data: 2022-02-20
"""

from __future__ import annotations

from .matrix import Matrix
from .vector import Vector

class BoolMatrix(Matrix[bool]):
    def print(matrix: BoolMatrix) -> None:
        """Rašo matricą į konsolę"""

        for row in matrix._container:
            print(' '.join(map(lambda item: '1' if item else '0', row)))

    def flip(self, vector: Vector) -> None:
        """Keičia matricos reikšmę į atvirkščią nurodytoje pozicijoje"""

        self._container[vector.i][vector.j] = not self._container[vector.i][vector.j]

    def __hash__(self) -> int:
        """Skaičiuoja matricos maišos (angl. hash) reikšmę"""

        array = [item for row in self._container for item in row]
        return sum(v << i for i, v in enumerate(array))

    def __eq__(self, other: object) -> bool:
        """Tikrina ar matricos yra lygios"""

        return isinstance(other, BoolMatrix) and self._container == other._container
