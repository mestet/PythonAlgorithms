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
    united_segments = []
    while segments:
        seg_a = segments.pop(0)
        print("Popping " + str(seg_a))
        j = 0
        while j < len(segments):
            seg_b = segments[j]
            ax, ay = seg_a[0], seg_a[1]
            bx, by = seg_b[0], seg_b[1]
            if bx <= ax <= by or ax <= bx <= ay:
                print("Found pair for " + str(seg_a) + " -> " + str(seg_b))
                seg_a = (min(ax, bx), max(ay, by))
                print("United pair: " + str(seg_a))
                del segments[j]
            else:
                j += 1
        print("Adding united segment: " + str(seg_a))
        united_segments += [seg_a]

    print("United segments:")
    print(united_segments)

    for seg in united_segments:
        result_sum += seg[1] - seg[0]

    return result_sum


input_data = eval(input())
print(segment_length_sum(input_data))
