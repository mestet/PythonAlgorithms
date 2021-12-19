# Объединение отрезков
# Вводится кортеж пар натуральных чисел.
# Это координаты отрезков на прямой.
# Рассмотрим объединение этих отрезков и найдём длину этого объединения
# (т. е. совокупную длину всех «закрашенных» нашими отрезками отрезков на прямой).
#
# Входные данные
# (66, 91), (152, 230), (21, 81), (323, 342), (158, 211), (286, 332), (294, 330), (18, 58), (183, 236)
# Результат работы
# 213
# Поскольку если отрезки объединить по пересечению, то получатся (18, 91), (152, 236), (286, 342)


def segment_length_sum(segments):
    segments = sorted(list(segments))
    result_sum = 0
    limit = len(segments)
    i = 0
    while i < limit:
        seg_a = segments[i]
        for j in range(i + 1, limit):
            seg_b = segments[j]
            ax, ay = seg_a[0], seg_a[1]
            bx, by = seg_b[0], seg_b[1]
            i = j
            if bx <= ay:
                seg_a = (min(ax, bx), max(ay, by))
            else:
                break
        else:
            i += 1
        result_sum += seg_a[1] - seg_a[0]

    return result_sum


input_data = eval(input())
print(segment_length_sum(input_data))
