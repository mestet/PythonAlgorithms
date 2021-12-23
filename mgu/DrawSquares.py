# Написать функцию squares(w,h,(X,Y,s,c),...) со следующими параметрами:
# w и h — ширина и высота «экрана»,
# за которыми следуют 0 или больше 4-элементных последовательностей вида (X,Y,s,c),
# где X и Y — координаты левого верхнего угла квадрата,
# s — длина его стороны (не меньше 1),
# c — символ которым он заполняется на экране.
# Функция должна выводить прямоугольник из h×w точек,
# на котором соответствующими символами «нарисованы» квадраты соответствующих размеров в соответствующих местах.
# Координаты левого верхнего угла поля — 0,0. Растут вправо вниз.
# Проверять, что квадраты не выходят за границы поля, не надо.


def print_block(plot, block):
    x = block[0]
    y = block[1]
    s = block[2]
    c = block[3]

    for i in range(y, y + s, 1):
        for j in range(x, x + s, 1):
            plot[i][j] = c

    return plot


def squares(w, h, *blocks):
    plot = init_plot(w, h)
    for block in blocks:
        plot = print_block(plot, block)
    print_plot(plot)


def init_plot(w, h):
    plot = []
    for i in range(h):
        row = ["."] * w
        plot += [row]
    return plot


def print_plot(plot):
    for row in plot:
        print(*row, sep='')


if __name__ == "__main__":
    eval(input())
