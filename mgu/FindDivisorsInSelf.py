# Цифроделители
# Написать функцию divdigit(N),
# которой передаётся произвольное натуральное число N,
# а в ответ функция возвращает количество цифр этого числа, являющихся её делителями.
#
# Примеры
# print(divdigit(312345)) -> 4
# поскольку 312345 делится без остатка на 3, 1, 3, 5


def divdigit(input_number):
    number_digits = list(map(int, str(input_number)))
    count = 0
    for digit in number_digits:
        if digit != 0 and input_number % digit == 0:
            count += 1
    return count


if __name__ == "__main__":
    eval(input())
