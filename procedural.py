"""Процедурное решение биквадратного уравнения."""

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
    if a == 0:
        if b == 0:
            return d, None if c == 0 else ()
        ys = (-c / b,)
    elif d < 0:
        return d, ()
    elif d == 0:
        ys = (-b / (2 * a),)
    else:
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
    a = number("A", args[0] if len(args) > 0 else None)
    b = number("B", args[1] if len(args) > 1 else None)
    c = number("C", args[2] if len(args) > 2 else None)
    d, roots = solve(a, b, c)
    print(f"Дискриминант: {d:g}")
    if roots is None:
        print("Подходит любое действительное x")
    elif roots:
        print("Корни:", *[f"{x:g}" for x in roots])
    else:
        print("Действительных корней нет")
