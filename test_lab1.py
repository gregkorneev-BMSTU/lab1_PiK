"""Минимальная проверка трёх реализаций лабораторной работы."""

import sys

from oop import BiquadraticEquation
from procedural import solve as procedural_solve


def check(solve):
    assert solve(1, -5, 4) == (9, (-2.0, -1.0, 1.0, 2.0))
    assert solve(1, 1, 1) == (-3, ())
    assert solve(1, 0, 0) == (0, (0.0,))


check(procedural_solve)
equation = BiquadraticEquation(1, -5, 4)
assert equation.discriminant == 9
assert equation.real_roots() == (-2.0, -1.0, 1.0, 2.0)
if sys.version_info >= (3, 10):
    from functional import solve as functional_solve
    check(functional_solve)
else:
    print("Функциональный вариант требует Python 3.10+ (match/case); проверка пропущена.")
print("Все проверки пройдены.")
