# In this problem, the programmer is supposed to solve the problem using product function of the itertools library
# The difficulty of the problem is EASY
# Link to the problem: https://www.hackerrank.com/challenges/itertools-permutations/problem
# All test cases passed

from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

ab = [a] + [b]
res = list(product(*ab))
t = tuple(i for i in res)
print(" ".join(map(str, t)))
