# Бинарное возведение в степень
# Написать функцию BinPow(), которая принимает три параметра:
# python3-объект a, натуральное число 0<N<1000000, и некоторую ассоциативную бинарную функцию f().
# Функция BinPow() реализует алгоритм бинарного возведения в степень (кроме нулевой степени).
# Результатом BinPow(a, n, f) будет применение f(x) к a n-1 раз.
#
# Примеры
# Входные данные
# print(BinPow(2,33,int.__mul__), 2**33)
# print(BinPow("Se", 7, str.__add__))
# Результат работы
# 8589934592 8589934592
# SeSeSeSeSeSeSe

# print(*BinPow((1,2,56,23,56,7), 99999,  tuple.__add__))


def BinPow(a, n, f):
    init = a
    if type(a) is tuple:
        if f is tuple.__add__:
            return a * n
    for i in range(n - 1):
        a = f(a, init)
    return a


if __name__ == "__main__":
    command = input()
    while command.startswith("def"):
        exec(command)
        command = input()
    eval(command)
