#
# You are given a string .
# Your task is to verify that  is a floating point number.
#
# In this task, a valid float number must satisfy all the following requirements:
# Number can start with '+', '-' or '.' symbol.
# Number must contain at least one decimal value.
# Number must have exactly one '.' symbol.
# Number must not give any exceptions when converted using float(x).
#
# Input Format
#
# The first line contains an integer 0 < T < 10, the number of test cases.
# The next T lines contains a string with test case.
#
# Output Format
# Output True or False for each test case.
#
# Sample Input:
# 4
# 4.0O0
# -1.00
# +4.54
# SomeRandomStuff
#
# Sample Output:
# False
# True
# True
# False
#

def is_floating_number(s: str):
    if '.' not in s:
        return False
    try:
        return type(float(s)) == float
    except ValueError:
        return False


if __name__ == '__main__':
    for i in range(int(input())):
        tc = input()
        print(is_floating_number(tc))
