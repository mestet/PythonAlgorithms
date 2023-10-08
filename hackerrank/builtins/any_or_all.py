# any()
# This expression returns True if any element of the iterable is true.
# If the iterable is empty, it will return False.
#
# all()
# This expression returns True if all the elements of the iterable are true.
# If the iterable is empty, it will return True.
#
# You are given a space separated list of integers.
# If all the integers are positive, then you need to check if any integer is a palindromic integer.
# The first line contains an integer. It is the total number of integers in the list.
# The second line contains the space separated list of integers.
# Print True if all the conditions of the problem statement are satisfied. Otherwise, print False.
#
# Sample Input
# 5
# 12 9 61 5 14
#
# Sample Output
# True
#
# Explanation:
# Condition 1: All the integers in the list are positive.
# Condition 2: 5 is a palindromic integer.
# Hence, the output is True.
#
# Can you solve this challenge in 3 lines of code or less?
# There is no penalty for solutions that are correct but have more than 3 lines.
#
n, line = input(), input()
print(('-' not in line) and any([(e == e[::-1]) for e in line.split(' ')]))
