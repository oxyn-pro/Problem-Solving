s = "ababcbacadefegdehijhklij"


# TC: O(n)
# SC: O(1)
def partitionLabels(s):
    hm = {}
    start = end = 0
    res = []

    for i, v in enumerate(s):
        hm[v] = i

    for i, v in enumerate(s):
        start += 1

        if hm[v] > end:
            end = hm[v]

        if i == end:
            res.append(start)
            start = 0

    return res


partitionLabels(s)
