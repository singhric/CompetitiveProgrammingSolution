# Given an Integer N, write a program to reverse it.

# Input
# The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer N.

# Output
# For each test case, display the reverse of the given number N, in a new line.

# Constraints
# 1 ≤ T ≤ 1000
# 1 ≤ N ≤ 1000000

# Example:

# Input
# 4
# 12345
# 31203
# 2123
# 2300

# Output
# 54321
# 30213
# 3212
# 32

for t in range(int(input())):
    son = 0
    a = list(input())
    a.reverse()
    strings = [str(integer) for integer in a]
    a_string = "".join(strings)
    an_integer = int(a_string)
    print(an_integer)