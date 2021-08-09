# The difficulty of the problem is EASY
# Link to the problem: https://www.hackerrank.com/challenges/migratory-birds/problem
# All test cases passed

us = int(input())

us = list(map(int, input().split()))

def migratoryBirds(us):
    dictt = {}
    for i in us:
        if i in dictt:
            dictt[i] += 1
        else:
            dictt[i] = 1

    ll = sorted(dictt.items(), key= lambda x: x[1])
    for i in ll:
        if i[1] == ll[-1][1] and i[0] < ll[-1][0]:
            return ll[-2][0]
    else:
        return ll[-1][0]

print(migratoryBirds(us))
