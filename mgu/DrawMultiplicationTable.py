from math import ceil


# Ввести два натуральных числа через запятую: N и M. Вывести таблицу умножения от 1 до N включительно в формате,
# представленном ниже. Количество столбцов в выводе должно быть наибольшим,
# но общая ширина строки не должна превышать M (предполагается, что M достаточно велико, чтобы вместить один столбец).
# Ширина колонок под сомножители и произведения должна соответствовать максимальной ширине
# соответствующего значения (даже если в данной колонке данного столбца эта ширина не достигается, см. пример).
# Таким образом все столбцы должны быть одинаковой ширины, без учёта пробелов в конце строк, которых быть не должно.
# Разделители вида "===…===" должны быть ширины M.


def draw_mult_table(n, m):
    separator(m)
    mt = init_mult_table(n)

    eq_size = len(mt[0]) + 2
    pack = m // eq_size
    if (pack * eq_size + pack - 2) > m:
        pack -= 1

    row_amount = int(ceil(n / pack))

    for block_row in range(row_amount):
        sep = " | "
        left = n * block_row * pack
        right = left + n * pack
        block = mt[left:right]
        for row in range(n):
            line = sep.join(block[row::n])
            print(f"{line:^}")
        separator(m)


def init_mult_table(n):
    mt = []
    vw = len(str(n))
    rw = len(str(n * n))
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            mt += [f"{i:>{vw}} * {j:<{vw}} = {i * j:<{rw}}"]
    return mt


def separator(w, s="="):
    print(f"{s * w}")


def print_table(mt):
    for row in mt:
        print(row)


if __name__ == "__main__":
    user_input = input()
    draw_mult_table(int(eval(user_input)[0]), int(eval(user_input)[1]))


# if __name__ == "__main__":
#     user_input = input()
#     while user_input:
#         draw_mult_table(int(eval(user_input)[0]), int(eval(user_input)[1]))
#         user_input = input()
