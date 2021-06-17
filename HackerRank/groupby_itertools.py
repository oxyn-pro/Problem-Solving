# In this problem, the programmer is supposed to solve the problem using groupby function of the itertools library
# The difficulty of the problem is MIDDLE
# Link to the problem: https://www.hackerrank.com/challenges/compress-the-string/problem
# All test cases passed

from itertools import groupby

k = input()

l = [list(g) for i,g in groupby(k)]

res = ''
for j in l:
    li = []
    li.append(len(j))
    li.append(int(j[0]))
    li = tuple(li)
    res += ''.join(str(li)) + " "
print(res)
