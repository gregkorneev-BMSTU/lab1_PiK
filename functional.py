"""Функциональное решение биквадратного уравнения."""

import math
import sys


def number(name, argument=None):
    while True:
        try:
            return float(argument if argument is not None else input(f"{name} = "))
        except ValueError:
            print("Введите число.")
            argument = None


def solve(a, b, c):
    d = b * b - 4 * a * c
    match (a, b, d):
        case (0, 0, _):
            return d, None if c == 0 else ()
        case (0, _, _):
            ys = (-c / b,)
        case (_, _, d) if d < 0:
            return d, ()
        case (_, _, 0):
            ys = (-b / (2 * a),)
        case (_, _, d):
            ys = ((-b - math.sqrt(d)) / (2 * a),
                  (-b + math.sqrt(d)) / (2 * a))

    roots = []
    for y in ys:
        if y == 0:
            roots.append(0)
        elif y > 0:
            roots += [-math.sqrt(y), math.sqrt(y)]
    return d, tuple(sorted(set(roots)))


if __name__ == "__main__":
    args = sys.argv[1:]
    values = [number(name, args[i] if i < len(args) else None)
              for i, name in enumerate("ABC")]
    d, roots = solve(*values)
    print(f"Дискриминант: {d:g}")
    match roots:
        case None:
            print("Подходит любое действительное x")
        case ():
            print("Действительных корней нет")
        case _:
            print("Корни:", *[f"{x:g}" for x in roots])
