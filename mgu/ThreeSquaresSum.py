import math


# Ввести произвольную последовательность (не обязательно кортеж) натуральных чисел, не превышающих 1000000.
# Вывести, сколько среди них различных чисел, являющихся суммой трёх квадратов
# 3, 4, 2, 9, 1, 5, 6, 7, 8, 3, 6
# Это 3=1+1+1, 6=1+1+4 и 9=1+4+4


def count_three_square_sum(numbers):
    m = max(numbers)
    square_sum_list = init_squares_list(m)

    intersection = square_sum_list & set(numbers)
    return len(intersection)


def init_squares_list(limit):
    square_parts = set()
    for a in range(1, int(math.sqrt(limit)) + 1):
        a_sq = a * a
        bl = int(math.sqrt(limit - a_sq)) + 1
        for b in range(a, bl):
            b_sq = b * b
            cl = int(math.sqrt(limit - a_sq - b_sq)) + 1
            for c in range(b, cl):
                square_sum = a_sq + b_sq + c * c
                square_parts.add(square_sum)
    return square_parts


if __name__ == "__main__":
    print(count_three_square_sum(list(eval(input()))))
