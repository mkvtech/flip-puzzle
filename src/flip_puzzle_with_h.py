"""
flip_puzzle_with_h.py

Autorius: Maksim Kulagin

Data: 2022-02-20
"""

import copy
from typing import Final

import lib.aima.search as aima

from .all_math import BoolMatrix, Vector

class FlipPuzzleState(BoolMatrix):
    """
    Šita klasė yra reikalinga nes PriorityQueue lygina būsenas ir
    BoolMatrix klasę neįmanoma palyginti.
    """

    def __lt__(self, other: object) -> bool:
        """Lygina būseną su kita būsena. Visada gražina False"""

        return False

class FlipPuzzle(aima.Problem): # type: ignore
    initial: Final[FlipPuzzleState]
    goal: Final[FlipPuzzleState]

    def __init__(self, initial: BoolMatrix):
        """Inicializuoja 'Flip' problemą"""

        self.initial = FlipPuzzleState(initial.size_i, initial.size_j, lambda vector: initial.get_at_vector(vector))
        self.goal = FlipPuzzleState(initial.size_i, initial.size_j, lambda _: False)

        self.all_actions = [vector for vector in initial.each_vector()]

    def actions(self, _: FlipPuzzleState) -> list[Vector]:
        """Gražina įmanomus veiksmus"""

        return self.all_actions

    def result(self, state: FlipPuzzleState, action: Vector) -> FlipPuzzleState:
        """Skaičiuoja ir gražina naują būseną, pritaikant veiksmą"""

        new_state = copy.deepcopy(state)

        new_state.flip(action)

        for neighbour in action.neighbours():
            if new_state.is_inside(neighbour):
                new_state.flip(neighbour)

        return new_state

    def goal_test(self, state: FlipPuzzleState) -> bool:
        """Tikrina, ar būseną yra paskutinė"""

        return state == self.goal

    def h(self, node: aima.Node) -> int:
        """Skaičiuoja būsenos heuristinę reikšmę. Mažesne reikšmė - geriau"""

        return sum(
            [node.state.get_at_vector(vector) == self.goal.get_at_vector(vector) for vector in node.state.each_vector()]
        )

    def print_initial_state(self) -> None:
        """Rašo pradinę būseną į konsolę"""

        BoolMatrix.print(self.initial)
