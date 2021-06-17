

from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

ab = [a] + [b]
res = list(product(*ab))
t = tuple(i for i in res)
print(" ".join(map(str, t)))
