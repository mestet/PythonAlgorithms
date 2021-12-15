from itertools import cycle

# Цифры по спирали
# Ввести целые M и N,
# вывести последовательность 0 1 2 3 4 5 6 7 8 9 0 1 2 3 … в виде спирали
# (по часовой стрелке, из верхнего левого угла) заполненной таблицы N×M (N строк, M столбцов).
# Не забываем про то, что M и N могут быть чётными, нечётными и неизвестно, какое больше.
#
# Пример
# Входные данные: 6,5
# Результат работы:
# 0 1 2 3 4 5
# 7 8 9 0 1 6
# 6 7 8 9 2 7
# 5 6 5 4 3 8
# 4 3 2 1 0 9


def print_spiral_matrix(n, m):
    matrix = init_matrix(n, m)

    # direction
    horizontal = cycle([1, 0, -1, 0])  # right 1, left -1, stay 0
    vertical = cycle([0, 1, 0, -1])  # down 1, up -1, stay 0

    hor_steps = cycle([i for i in range(n, -1, -1)])
    ver_steps = cycle([i for i in range(m - 1, -1, -1)])
    steps = cycle([hor_steps, ver_steps])

    x = -1
    y = 0
    num = cycle(i for i in range(10))

    steps_to_make = next(next(steps))
    while steps_to_make > 0:
        dx = next(horizontal)
        dy = next(vertical)
        for i in range(steps_to_make):
            x += dx
            y += dy
            matrix[y][x] = next(num)
        steps_to_make = next(next(steps))

    print_matrix(matrix)


def print_matrix(matrix):
    for row in matrix:
        print(*row)


def init_matrix(columns, rows):
    matrix = []
    for i in range(rows):
        row = [0] * columns
        matrix += [row]
    return matrix


input_n, input_m = eval(input())
print_spiral_matrix(input_n, input_m)
