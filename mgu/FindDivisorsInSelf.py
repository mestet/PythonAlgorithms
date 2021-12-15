# Цифроделители
# Написать функцию divdigit(N),
# которой передаётся произвольное натуральное число N,
# а в ответ функция возвращает количество цифр этого числа, являющихся её делителями.
#
# Примеры
# 312345 -> 4
# поскольку 312345 делится без остатка на 3, 1, 3, 5


def find_divisors(input_number):
    number_digits = list(map(int, str(input_number)))
    count = 0
    for digit in number_digits:
        if input_number % digit == 0:
            count += 1
    print(count)


find_divisors(int(input()))
