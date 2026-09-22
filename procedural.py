"""Решение биквадратного уравнения в процедурном стиле."""

import math
import sys


def read_coefficient(name, value=None):
    """Возвращает вещественный коэффициент, повторяя ввод при ошибке."""
    while True:
        raw = value if value is not None else input(f"Введите {name}: ")
        try:
            return float(raw)
        except (TypeError, ValueError):
            print(f"{raw!r} не является вещественным числом.")
            value = None


def roots_from_y(values):
    roots = []
    for y in values:
        if y == 0:
            roots.append(0.0)
        elif y > 0:
            root = math.sqrt(y)
            roots.extend((-root, root))
    return tuple(sorted(set(roots)))


def solve(a, b, c):
    """Возвращает дискриминант и действительные корни A*x**4+B*x**2+C=0."""
    discriminant = b * b - 4 * a * c
    if a == 0:
        if b == 0:
            return discriminant, None if c == 0 else ()
        return discriminant, roots_from_y((-c / b,))
    if discriminant < 0:
        return discriminant, ()
    if discriminant == 0:
        return discriminant, roots_from_y((-b / (2 * a),))
    root_d = math.sqrt(discriminant)
    return discriminant, roots_from_y(((-b - root_d) / (2 * a),
                                        (-b + root_d) / (2 * a)))


def print_answer(discriminant, roots):
    print(f"Дискриминант: {discriminant:g}")
    if roots is None:
        print("Уравнение верно при любом действительном x.")
    elif roots:
        print("Действительные корни:", ", ".join(f"{root:g}" for root in roots))
    else:
        print("Действительных корней нет.")


def main(arguments=None):
    arguments = sys.argv[1:] if arguments is None else arguments
    values = list(arguments[:3]) + [None] * 3
    coefficients = [read_coefficient(name, value)
                    for name, value in zip("ABC", values)]
    print_answer(*solve(*coefficients))


if __name__ == "__main__":
    main()
