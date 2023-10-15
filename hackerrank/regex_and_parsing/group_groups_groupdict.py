import re


def example():
    text = 'max@hackerrank.com'
    pattern = r'(\w+)@(\w+)\.(\w+)'
    m = re.match(pattern, text)
    # The entire match
    print(m.group(0))  # 'max@hackerrank.com'

    # The n-th parenthesized subgroup.
    print(m.group(1))  # 'max'
    print(m.group(3))  # 'com'

    # Multiple arguments give us a tuple.
    print(m.group(1, 2, 3))  # ('max', 'hackerrank', 'com')

    # A groups() expression returns a tuple containing all the subgroups of the match.
    print(m.groups())  # ('max', 'hackerrank', 'com')

    named_pattern = r'(?P<user>\w+)@(?P<website>\w+)\.(?P<domain>\w+)'
    nm = re.match(named_pattern, text)

    # A groupdict() expression returns a dictionary containing all the named subgroups of the match,
    # keyed by the subgroup name.
    print(nm.groupdict())  # {'website': 'hackerrank', 'user': 'max', 'domain': 'com'}


# You are given a string S.
# Your task is to find the first occurrence of an alphanumeric character
# in S (read from left to right) that has consecutive repetitions.
def task(text):
    pattern = r'([a-z,A-Z,0-9])\1+'
    m = re.search(pattern, text)
    if m:
        print(m.group(1))
    else:
        print(-1)


if __name__ == '__main__':
    tc = [
        '..123456778910111213141516171820212223',
        '__init__',
        'This is a sample string with repeetitive characters like oo, nnn, and 11'
    ]

    for t in tc:
        task(t)
