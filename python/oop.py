def read_number(name):
    # Просим ввести коэффициент заново, если преобразование в число не удалось.
    while True:
        try:
            return int(input("Введите " + name + ": "))
        except ValueError:
            print("Введите число")


def print_roots(y):
    # Переводим найденное y обратно в действительные значения x.
    if y > 0:
        x = y ** 0.5
        print("Корни:", x, -x)
        return True
    elif y == 0:
        print("Корень: 0")
        return True
    # Отрицательное y не даёт действительных x.
    return False


class BiquadraticEquation:
    def __init__(self, a, b, c):
        # Сохраняем коэффициенты в объекте.
        self.a = a
        self.b = b
        self.c = c

    def solve(self):
        # Считаем дискриминант уравнения относительно y = x^2.
        d = self.b * self.b - 4 * self.a * self.c
        print("Дискриминант:", d)

        # При A = 0 остаётся линейное уравнение относительно y.
        if self.a == 0:
            if self.b == 0:
                if self.c == 0:
                    print("Подходит любое действительное x")
                else:
                    print("Корней нет")
            else:
                y1 = -self.c / self.b
                # Выводим x для найденного значения y.
                if not print_roots(y1):
                    print("Действительных корней нет")
            return

        # Для отрицательного дискриминанта действительных корней нет.
        if d < 0:
            print("Действительных корней нет")
            return
        elif d == 0:
            # При нулевом дискриминанте находим одно значение y.
            y1 = -self.b / (2 * self.a)
            if not print_roots(y1):
                print("Действительных корней нет")

        else:
            # При положительном дискриминанте находим два значения y.
            y1 = (-self.b + d ** 0.5) / (2 * self.a)
            y2 = (-self.b - d ** 0.5) / (2 * self.a)

            # Печатаем корни для каждого y и проверяем, нашёлся ли хотя бы один.
            has_roots = print_roots(y1)
            if print_roots(y2):
                has_roots = True
            if not has_roots:
                print("Действительных корней нет")


def main():
    # Получаем три коэффициента с клавиатуры.
    a = read_number("A")
    b = read_number("B")
    c = read_number("C")

    # Создаём объект с коэффициентами и вызываем его метод решения.
    equation = BiquadraticEquation(a, b, c)
    equation.solve()


if __name__ == "__main__":
    # Запускаем программу.
    main()
