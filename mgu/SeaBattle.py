# Морской бой
# Ввести несколько строк одинаковой длины, состоящих из символов '#' и '.'.
# Первый и последний символ каждой строки — '.', а первая и последняя строки состоят целиком из '-'.
# Известно (проверять не надо), что на получившемся поле изображены только прямоугольники,
# причём они не соприкасаются даже углами. Вывести количество этих прямоугольников.
#
# Примеры
# Входные данные
# ------------
# .###.....#..
# .###.##..#..
# .....##.....
# .....##..#..
# ............
# ............
# .####..####.
# .......####.
# .......####.
# ------------
# Результат работы
# 6

def count_ships(input_matrix):
    ship_count = 0
    for y in range(len(input_matrix)):
        line = input_matrix[y]
        end_x = len(line)

        x = 0
        while x < end_x:
            ch = line[x]
            if ch == '#':
                start_x = x
                while ch == '#' and x < end_x:
                    x += 1
                    ch = line[x]
                if y == 0:
                    ship_count += 1
                if y > 0:
                    prev_line = input_matrix[y - 1]
                    if prev_line[start_x] != '#':
                        ship_count += 1
            x += 1
    return ship_count


def read_input():
    result = []
    start = input()
    if start[0] == '-':
        line = input()
        while line[0] != '-':
            result += [line]
            line = input()
    return result


if __name__ == "__main__":
    print(count_ships(read_input()))
