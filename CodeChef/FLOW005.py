# Consider a currency system in which there are notes of six denominations, namely, Rs. 1, Rs. 2, Rs. 5, Rs. 10, Rs. 50, Rs. 100.
# If the sum of Rs. N is input, write a program to computer smallest number of notes that will combine to give Rs. N.

# Input
# The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer N.

# Output
# For each test case, display the smallest number of notes that will combine to give N, in a new line.

# Constraints
# 1 ≤ T ≤ 1000
# 1 ≤ N ≤ 1000000
# Example
# Input
# 3 
# 1200
# 500
# 242

# Output
# 12
# 5
# 7

for t in range(int(input())):
    n = int(input())
    notes = 0
    if n >= 100:
        notes = n//100
        n = n % 100
    if n >= 50:
        notes = notes + (n//50)
        n = n%50
    if n >= 10:
        notes = notes + (n//10)
        n = n%10
    if n >= 5:
        notes = notes + (n//5)
        n = n%5
    if n >= 2:
        notes = notes + (n//2)
        n = n%2
    if n >= 1:
        notes = notes + (n//1)
        n = n%1
    print(notes)

    
