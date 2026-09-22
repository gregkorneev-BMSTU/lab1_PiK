"""Решение биквадратного уравнения в функциональном стиле с match/case."""

import math
import sys


def read_coefficient(name, value=None):
    while True:
        raw = value if value is not None else input(f"Введите {name}: ")
        try:
            return float(raw)
        except (TypeError, ValueError):
            print(f"{raw!r} не является вещественным числом.")
            value = None


def roots_from_y(values):
    return tuple(sorted({root for y in values for root in
                         ((0.0,) if y == 0 else (-math.sqrt(y), math.sqrt(y)) if y > 0 else ())}))


def solve(a, b, c):
    discriminant = b * b - 4 * a * c
    match (a == 0, b == 0, discriminant):
        case (True, True, _):
            return discriminant, None if c == 0 else ()
        case (True, False, _):
            return discriminant, roots_from_y((-c / b,))
        case (False, _, d) if d < 0:
            return discriminant, ()
        case (False, _, 0):
            return discriminant, roots_from_y((-b / (2 * a),))
        case (False, _, d):
            root_d = math.sqrt(d)
            return discriminant, roots_from_y(((-b - root_d) / (2 * a),
                                                (-b + root_d) / (2 * a)))


def main(arguments=None):
    arguments = sys.argv[1:] if arguments is None else arguments
    values = list(arguments[:3]) + [None] * 3
    discriminant, roots = solve(*(read_coefficient(name, value)
                                  for name, value in zip("ABC", values)))
    print(f"Дискриминант: {discriminant:g}")
    match roots:
        case None:
            print("Уравнение верно при любом действительном x.")
        case ():
            print("Действительных корней нет.")
        case _:
            print("Действительные корни:", ", ".join(f"{root:g}" for root in roots))


if __name__ == "__main__":
    main()
