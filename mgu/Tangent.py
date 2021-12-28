# Ввести числа: разциональное A — угол из диапазона от 1 до 99 градов (десятичных градусов),
# и натуральное 4 ⩽ E ⩽ 1000 — точность вычисления (в терминах контекста вычислений модуля Decimal — поле perc).
# Вычислить значение тангенса с указанной точностью.
# Число Пи (если оно вам понадобится) тоже надо вычислять!
import decimal
import math
from decimal import Decimal, getcontext


def tangent(grad_angle, decimal_places):
    getcontext().prec = 2000
    getcontext().rounding = decimal.ROUND_HALF_UP
    rad_angle = (Decimal(grad_angle) * calc_pi()) / 200  # gradian to radian

    sin = calc_sin(rad_angle)
    cos = calc_cos(rad_angle)
    getcontext().prec = decimal_places
    return sin / cos


def calc_sin(x):
    sin_sum = Decimal(x)
    sign = -1
    for i in range(1, 200):
        sin_sum += sign * (x ** (2 * i + 1)) / Decimal(math.factorial(2 * i + 1))
        sign *= -1
    return sin_sum


def calc_cos(x):
    cos_sum = Decimal(1)
    sign = -1
    for i in range(1, 200):
        cos_sum += sign * (x ** (2 * i)) / Decimal(math.factorial(2 * i))
        sign *= -1
    return cos_sum


# Chudnovsky algorithm
def calc_pi():
    const = Decimal(426880) * Decimal.sqrt(Decimal(10005))
    lq = Decimal(13591409)
    xq = Decimal(1)
    mq = Decimal(1)
    kq = Decimal(-6)
    q_sum = lq
    for i in range(1, 100):
        q = Decimal(i)
        lq += 545140134
        xq *= -262537412640768000
        kq += 12
        mq *= ((kq * kq * kq) - 16 * kq) / (q * q * q)
        q_sum += (mq * lq) / xq
    return const / q_sum


if __name__ == "__main__":
    u_grad_angle = input()
    u_precision = int(input())
    print(tangent(u_grad_angle, u_precision))
