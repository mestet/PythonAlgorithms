# Дано целое число n, 0 ≤ n ≤ 11.
# Требуется вывести все правильные(лексикографически) скобочные последовательности длины 2 ⋅ n,
# В задаче используются только круглые скобки.
# Example:
# 3
# ((()))
# (()())
# (())()
# ()(())
# ()()()


def print_all_balanced_sequences(n):
    s = n * 2
    brackets = init_brackets(s)
    while brackets:
        print_brackets(brackets)
        brackets = next_balanced_sequence(brackets)


def next_balanced_sequence(base_seq):
    next_seq = []
    length = len(base_seq)
    depth = 0

    for i in range(length - 1, -1, -1):
        if base_seq[i] == '(':
            depth -= 1
        else:
            depth += 1

        if base_seq[i] == '(' and depth > 0:
            depth -= 1
            left = (length - i - 1 - depth) // 2
            right = length - i - 1 - left

            next_seq += base_seq[0: i]
            next_seq += [')']
            next_seq += ['('] * left
            next_seq += [')'] * right
            break

    return next_seq


def print_brackets(brackets):
    for i in brackets:
        print(i, sep='', end='')
    print(end='\n')


def init_brackets(size):
    result = []
    for i in range(size // 2):
        result += ['(']
    for i in range(size // 2):
        result += [')']
    return result


if __name__ == "__main__":
    input_num = int(input())
    print_all_balanced_sequences(input_num)
