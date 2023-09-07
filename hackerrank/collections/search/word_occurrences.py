from collections import OrderedDict


# You are given n words. Some words may repeat.
# For each word, output its number of occurrences.
# The output order should correspond with the input order of appearance of the word.
# Output:
# First line - the number of distinct words from the input.
# Second line - the number of occurrences for each distinct word according to their appearance in the input.

# Expecting: "3\n2 1 1\n"
smoke_dataset = """4
bcdef
abcdefg
bcde
bcdef"""

def process(lines=0):
    od = OrderedDict()
    for i in range(lines):
        ln = input()
        if ln not in od:
            od.update({ln: 1})
        else:
            val = od.get(ln) + 1
            od.update({ln: val})
    print(len(od))
    print(' '.join([str(_) for _ in od.values()]))


if __name__ == '__main__':
    n = int(input())
    process(n)
