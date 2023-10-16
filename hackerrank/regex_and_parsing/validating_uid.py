import re


def validate_line(line):
    return bool(re.match(r'^(?=(?:[^A-Z]*[A-Z]){2})(?=(?:\D*\d){3})(?!.*(.).*\1)[A-Za-z\d]{10}$',
                         line))


tests = [input() for _ in range(int(input()))]
for t in tests:
    if validate_line(t):
        print('Valid')
    else:
        print('Invalid')
