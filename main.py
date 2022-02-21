"""
main.py

Autorius: Maksim Kulagin

Data: 2022-02-20
"""

import random
from typing import Any, Callable

import lib.aima.search as aima

from src.all_math import BoolMatrix, Vector
from src.flip_puzzle import FlipPuzzle
# from src.flip_puzzle_with_h import FlipPuzzle
# from src.flip_puzzle_optimized import FlipPuzzle

def decode_problem(string: str) -> FlipPuzzle:
    """Sukūria 'FlipPuzzle' objektą iš teksto eilutės"""

    encoded_rows = string.split(' ')

    initializer = lambda vector: encoded_rows[vector.i][vector.j] == '1'
    return FlipPuzzle(BoolMatrix(len(encoded_rows), len(encoded_rows[0]), initializer))

def generate_random_problem(size_i: int, size_j: int) -> FlipPuzzle:
    """Sukūria atsitiktinį 'FlipPuzzle' objektą"""

    return FlipPuzzle(BoolMatrix(size_i, size_j, lambda _: random.choice([True, False])))

def print_solution(solution: list[Vector]) -> None:
    """Gražiai rašo sprendimą į konsolę"""

    print(', '.join(map(lambda vector: f'({vector.j + 1} {vector.i + 1})', solution)))

def solve(problem: aima.Problem, algorithm: Callable[[aima.Problem], list[Vector]]) -> Any:
    """Išsprendžia 'Flip' problemą ir rašo sprendimą į konsolę"""

    print('Problem:')
    problem.print_initial_state()

    print('Solving...')
    solution = algorithm(problem)

    print('Solution:')
    print_solution(solution)

    return solution

def time_test() -> None:
    """Skaičiuoja kiek laiko užtrunka sprendimas"""

    import timeit

    # problem = decode_problem('110 100 000')
    problem = generate_random_problem(3, 3)

    print('Timing...')
    print(timeit.timeit(lambda: aima.best_first_graph_search(problem, problem.h).solution(), number = 1))

def main() -> None:
    """Programos pradžia"""

    solve(
        decode_problem('000 110 000'),
        lambda problem: aima.breadth_first_graph_search(problem).solution() # type: ignore
    )

    # solve(
    #     generate_random_problem(3, 3),
    #     lambda problem: aima.breadth_first_graph_search(problem).solution() # type: ignore
    # )

    # time_test()

if __name__ == '__main__':
    main()
