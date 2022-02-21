"""
flip_puzzle.py

Autorius: Maksim Kulagin

Data: 2022-02-20
"""

import copy
from typing import Final

import lib.aima.search as aima

from .all_math import BoolMatrix, Vector

class FlipPuzzle(aima.Problem): # type: ignore
    initial: Final[BoolMatrix]
    goal: Final[BoolMatrix]

    def __init__(self, initial: BoolMatrix):
        """Inicializuoja 'Flip' problemą"""

        self.initial = initial
        self.goal = BoolMatrix(initial.size_i, initial.size_j, lambda _: False)

        self.all_actions = [vector for vector in initial.each_vector()]

    def actions(self, _: BoolMatrix) -> list[Vector]:
        """Gražina įmanomus veiksmus"""

        return self.all_actions

    def result(self, state: BoolMatrix, action: Vector) -> BoolMatrix:
        """Skaičiuoja ir gražina naują būseną, pritaikant veiksmą"""

        new_state = copy.deepcopy(state)

        new_state.flip(action)

        for neighbour in action.neighbours():
            if new_state.is_inside(neighbour):
                new_state.flip(neighbour)

        return new_state

    def goal_test(self, state: BoolMatrix) -> bool:
        """Tikrina, ar būseną yra paskutinė"""

        return state == self.goal

    def print_initial_state(self) -> None:
        """Rašo pradinę būseną į konsolę"""

        BoolMatrix.print(self.initial)
