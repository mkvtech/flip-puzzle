"""
flip_puzzle_optimized.py

Autorius: Maksim Kulagin

Data: 2022-02-20
"""

from __future__ import annotations
import copy

import lib.aima.search as aima

from .all_math import BoolMatrix, Vector

class FlipPuzzleState:
    matrix: BoolMatrix
    used_actions: set[Vector]

    def __init__(self, matrix: BoolMatrix, used_actions: set[Vector]):
        """Inicializuoja 'Flip' problemos būseną"""

        self.matrix = matrix
        self.used_actions = used_actions

    def apply(self, action: Vector) -> FlipPuzzleState:
        """
        Skaičiuoja ir gražina naują būseną, pritaikant veiksmą. Pridėda veiksmą
        prie panaudotų veiksmų
        """

        new_matrix = copy.deepcopy(self.matrix)

        new_matrix.flip(action)

        for neighbour in action.neighbours():
            if new_matrix.is_inside(neighbour):
                new_matrix.flip(neighbour)

        new_used_actions = self.used_actions.copy()
        new_used_actions.add(action)
        return FlipPuzzleState(new_matrix, new_used_actions)

    def __hash__(self) -> int:
        """Skaičiuoja būsenos maišos (angl. hash) reikšmę"""

        return hash(self.matrix)

    def __eq__(self, other: object) -> bool:
        """Tikrina ar būsenos yra lygios"""

        return isinstance(other, FlipPuzzleState) and self.matrix == other.matrix

    def __lt__(self, other: FlipPuzzleState) -> bool:
        """
        Lygina būseną su kita būsena. Visada gražina False. Šis metodas
        reikalingas PriorityQueue klasėje
        """

        return False

class FlipPuzzle(aima.Problem): # type: ignore
    initial: FlipPuzzleState
    goal: FlipPuzzleState
    all_actions: set[Vector]

    def __init__(self, initial: BoolMatrix):
        """Inicializuoja 'Flip' problemą"""

        self.initial = FlipPuzzleState(initial, set())
        self.goal = FlipPuzzleState(BoolMatrix(initial.size_i, initial.size_j, lambda vector: False), set())
        self.all_actions = set([vector for vector in initial.each_vector()])

    def actions(self, state: FlipPuzzleState) -> set[Vector]:
        """Gražina įmanomus veiksmus"""

        return self.all_actions - state.used_actions

    def result(self, state: FlipPuzzleState, action: Vector) -> FlipPuzzleState:
        """Skaičiuoja ir gražina naują būseną, pritaikant veiksmą"""

        return state.apply(action)

    def goal_test(self, state: FlipPuzzleState) -> bool:
        """Tikrina, ar būseną yra paskutinė"""

        return state.matrix == self.goal.matrix

    def h(self, node: aima.Node) -> int:
        """Skaičiuoja būsenos heuristinę reikšmę. Mažesne reikšmė - geriau"""

        return sum(
            [node.state.matrix.get_at_vector(vector) == self.goal.matrix.get_at_vector(vector) for vector in node.state.matrix.each_vector()]
        )

    def print_initial_state(self) -> None:
        """Rašo pradinę būseną į konsolę"""

        BoolMatrix.print(self.initial.matrix)
