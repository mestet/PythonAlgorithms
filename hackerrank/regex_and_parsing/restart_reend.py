import re


def process(input_string='aaadaa', substring='aa'):
    patt = f'(?=({re.escape(substring)}))'
    res = [(_.start(1), _.end(1) - 1) for _ in re.finditer(patt, input_string)]

    if not res:
        res = [(-1, -1)]

    for it in res:
        print(it)


if __name__ == '__main__':
    a, b = input(), input()
    process(a, b)
