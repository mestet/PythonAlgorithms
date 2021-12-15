# Бинарное возведение в степень
# Написать функцию BinPow(), которая принимает три параметра:
# python3-объект a, натуральное число 0<N<1000000, и некоторую ассоциативную бинарную функцию f().
# Функция BinPow() реализует алгоритм бинарного возведения в степень (кроме нулевой степени).
# Результатом BinPow(a, n, f) будет применение f(x) к a n-1 раз.
#
# Примеры
# Входные данные
# print(BinPow(2,33,int.mul), 2**33)
# print(BinPow("Se", 7, str.add))
# Результат работы
# 8589934592 8589934592
# SeSeSeSeSeSeSe


def bin_pow(a, n, f):
    init = a
    for i in range(n - 1):
        a = f(a, init)
    return a


print(bin_pow(2, 33, int.__mul__))
print(bin_pow(11, 2, int.__mul__))
print(bin_pow(256, 3, int.__sub__))
print(bin_pow(256, 256, int.__add__))
print(bin_pow("Se", 7, str.__add__))
print(bin_pow("Wv", 1, str.__add__))
print(bin_pow("Wv", 0, str.__add__))
