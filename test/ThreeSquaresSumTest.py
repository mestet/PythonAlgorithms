import time

from mgu import ThreeSquaresSum
from guppy import hpy

h = hpy()


def test():
    cases = {
        ("3, 4, 2, 9, 1, 5, 6, 7, 8, 3, 6", 3),
        ("(1+i%10 for i in range(100000))", 3),
        ("[7,7,7,7,7,7,7,7,7,7]", 0),
        ("range(100,500,3) # Just text", 101),
        ('__import__("itertools").chain(range(1,10050,101),range(7000,9900,117))', 103)
    }

    for tc in cases:
        ts = time.time_ns()
        act = ThreeSquaresSum.count_three_square_sum(list(eval(tc[0])))
        elapsed = (time.time_ns()) - ts

        tr = "passed" if act == tc[-1] else "failed"
        print(f"Test {tr}. Took {elapsed} ns:\n{tc[0]}\n{act}\n{'='*120}")


if __name__ == "__main__":
    test()
