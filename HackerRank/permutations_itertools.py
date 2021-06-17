# In this problem, the programmer is supposed to solve the problem using permutations function of the itertools library
# The difficulty of the problem is EASY
# Link to the problem: https://www.hackerrank.com/challenges/itertools-permutations/problem
# All test cases passed

from itertools import permutations

usim = input().split()

res = sorted(list(permutations(usim[0], int(usim[1]))))

for i in res:
    print("".join(i[:]))
