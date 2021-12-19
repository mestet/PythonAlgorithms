from math import sin, cos


# 'Вектор функций'
#
# Написать функцию superposition(funmod, funseq),
# которая принимает два параметра — функцию funmod() от одного переменного,
# и последовательность funseq[] функций от одного переменного.
#
# superposition() возвращает также список функций funres[],
# каждая из которых представляет собой суперпозицию вида funres[i] ::== funmod(funseq[i])
#
# Input:
#    1 from math import *
#    2 F = superposition(abs, (sin, cos))
#    3 print(F[0](-1), F[1](-1), F[0](2), F[1](2))
# Output:
# 0.8414709848078965 0.5403023058681398 0.9092974268256817 0.4161468365471424


def superposition(funmod, funseq):
    def inner(x):
        return [funmod(f(x)) for f in funseq]
    return inner


if __name__ == "__main__":
    F = superposition(abs, (sin, cos))
    print(F(-1)[0], F(-1)[1], F(2)[0], F(2)[1])
