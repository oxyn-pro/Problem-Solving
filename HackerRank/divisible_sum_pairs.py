# The link for a problem: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
# The difficulty of the problem is EASY
# All test cases passed

def divisibleSumPairs(n, k, lst):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if (lst[i] + lst[j]) % k == 0:
                count += 1
    return count
