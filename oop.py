"""Объектно-ориентированное решение биквадратного уравнения."""

import math
import sys


class Equation:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def roots(self):
        d = self.b ** 2 - 4 * self.a * self.c
        if self.a == 0:
            if self.b == 0:
                return d, None if self.c == 0 else ()
            ys = (-self.c / self.b,)
        elif d < 0:
            return d, ()
        elif d == 0:
            ys = (-self.b / (2 * self.a),)
        else:
            ys = ((-self.b - math.sqrt(d)) / (2 * self.a),
                  (-self.b + math.sqrt(d)) / (2 * self.a))

        roots = []
        for y in ys:
            if y == 0:
                roots.append(0)
            elif y > 0:
                roots += [-math.sqrt(y), math.sqrt(y)]
        return d, tuple(sorted(set(roots)))


def number(name, argument=None):
    while True:
        try:
            return float(argument if argument is not None else input(f"{name} = "))
        except ValueError:
            print("Введите число.")
            argument = None


if __name__ == "__main__":
    args = sys.argv[1:]
    values = [number(name, args[i] if i < len(args) else None)
              for i, name in enumerate("ABC")]
    d, roots = Equation(*values).roots()
    print(f"Дискриминант: {d:g}")
    if roots is None:
        print("Подходит любое действительное x")
    elif roots:
        print("Корни:", *[f"{x:g}" for x in roots])
    else:
        print("Действительных корней нет")
