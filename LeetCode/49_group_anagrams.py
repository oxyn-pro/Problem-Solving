strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


# TC: O(n k)
# SC: O(n)
def groupAnagrams(strs):
    hm = {}
    res = []

    for s in strs:
        count = [0] * 26

        for c in s:
            count[ord(c) - 97] += 1

        count = tuple(count)

        if count in hm:
            hm[count].append(s)
        else:
            hm[count] = [s]

    for i, v in hm.items():
        res.append(v)

    return res


groupAnagrams(strs)


### SOLUTION 2 ###
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# TC: O(n k log k)
# SC: O(n)
def groupAnagrams_LK(strs):
    hm = {}
    res = []

    for i in range(len(strs)):
        w = "".join(sorted(strs[i]))

        if w in hm:
            root = hm[w]
            while root.next:
                root = root.next
            root.next = ListNode(strs[i])
        else:
            hm[w] = ListNode(strs[i])

    for i, v in hm.items():
        node = v
        group = []
        while node:
            group.append(node.val)
            node = node.next
        res.append(group)

    return res


groupAnagrams_LK(strs)
