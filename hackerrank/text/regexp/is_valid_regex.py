import re


# You are given a string .
# Your task is to find out whether  is a valid regex or not.


def is_valid_regex(regex_pattern):
    try:
        re.compile(regex_pattern)
        return True
    except re.error:
        return False


def process():
    n = int(input())
    for i in range(n):
        regexp = input()
        print(is_valid_regex(regexp))


if __name__ == '__main__':
    process()
