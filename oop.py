"""Решение биквадратного уравнения в объектно-ориентированном стиле."""

import math
import sys


class BiquadraticEquation:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    @property
    def discriminant(self):
        return self.b ** 2 - 4 * self.a * self.c

    @staticmethod
    def _roots_from_y(values):
        roots = []
        for y in values:
            if y == 0:
                roots.append(0.0)
            elif y > 0:
                root = math.sqrt(y)
                roots.extend((-root, root))
        return tuple(sorted(set(roots)))

    def real_roots(self):
        if self.a == 0:
            if self.b == 0:
                return None if self.c == 0 else ()
            return self._roots_from_y((-self.c / self.b,))
        if self.discriminant < 0:
            return ()
        if self.discriminant == 0:
            return self._roots_from_y((-self.b / (2 * self.a),))
        root_d = math.sqrt(self.discriminant)
        return self._roots_from_y(((-self.b - root_d) / (2 * self.a),
                                   (-self.b + root_d) / (2 * self.a)))


def read_coefficient(name, value=None):
    while True:
        raw = value if value is not None else input(f"Введите {name}: ")
        try:
            return float(raw)
        except (TypeError, ValueError):
            print(f"{raw!r} не является вещественным числом.")
            value = None


def main(arguments=None):
    arguments = sys.argv[1:] if arguments is None else arguments
    values = list(arguments[:3]) + [None] * 3
    equation = BiquadraticEquation(*(read_coefficient(name, value)
                                     for name, value in zip("ABC", values)))
    print(f"Дискриминант: {equation.discriminant:g}")
    roots = equation.real_roots()
    if roots is None:
        print("Уравнение верно при любом действительном x.")
    elif roots:
        print("Действительные корни:", ", ".join(f"{root:g}" for root in roots))
    else:
        print("Действительных корней нет.")


if __name__ == "__main__":
    main()
