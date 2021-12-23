# Ввести строку, содержащую произвольные символы (кроме символа «@»).
# Затем ввести строку-шаблон, которая может содержать символы '@'.
# Проверить, содержится ли в исходной строке подстрока, совпадающая со строкой-шаблоном везде, кроме символов '@';
# на месте '@' в исходной строке должен стоять ровно один произвольный символ.
# Вывести наименьшую позицию в строке, с которой начинается эта подстрока, или '-1', если её там нет.
# Использовать регулярные выражения нельзя! ☺


def find_pattern(base, pattern):
    splitted = pattern.split("@")
    skip = 0
    for ps in splitted:
        if ps:
            s0 = ps
            break
        skip += 1
    else:
        return 0

    start_at = base.find(s0) - skip
    if start_at < 0:
        return -1

    while start_at > 0:
        start = start_at
        for sn in splitted:
            if not sn:
                start += 1
                continue
            if compare_substring(base, sn, start):
                start += len(sn) + 1
            else:
                start_at = base.find(s0, start_at + len(s0))
                break
        else:
            return start_at
    return -1


def compare_substring(base, sub, start):
    if len(sub) >= len(base):
        return False
    for i in range(len(sub)):
        if sub[i] != base[start + i]:
            return False
    else:
        return True


if __name__ == "__main__":
    b = input()
    p = input()
    print(find_pattern(b, p))
