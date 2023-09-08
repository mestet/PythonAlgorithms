from collections import deque


def process(n=0):
    dq = deque()
    for i in range(n):
        words = input().split(' ')
        if len(words) == 1:
            eval(f'dq.{words[0]}()')

        if len(words) == 2:
            eval(f'dq.{words[0]}({words[1]})')

    print(' '.join([str(_) for _ in dq]))


if __name__ == '__main__':
    n = int(input())
    process(n)
