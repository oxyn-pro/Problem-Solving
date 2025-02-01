s = "cbaebabacd"
p = "abc"


# TC: O(n x k)
# SC: O(n x k)
def findAnagrams(s, p):
    """
    This Solution uses hashmap to store count of the string ie:
        {
            "aa" : [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        }
    """

    def count(s):
        count = [0] * 26

        for c in s:
            count[ord(c) - 97] += 1

        return count

    def is_anagram(s, p_count, hm):
        if s not in hm:
            hm[s] = count(s)

        return hm[s] == p_count

    left = 0
    p_count = count(p)
    hm = {}
    res = []

    for right in range(len(s)):
        if right - left == len(p) - 1:
            if is_anagram(s[left : right + 1], p_count, hm):
                res.append(left)
            left += 1
    return res


findAnagrams(s, p)


# TC: O(n)
# SC: O(n) - worst case, if all substrings are anagrams. But in general it is O(1)
def findAnagrams(s, p):
    """
    This solution is better because we do not need to generate count string
    every time when s_length length meets p_length
    """
    s_count = {}
    p_count = {}
    res = []
    left = 0

    for i in p:
        if i in p_count:
            p_count[i] += 1
        else:
            p_count[i] = 1

    for right in range(len(s)):
        if s[right] in s_count:
            s_count[s[right]] += 1
        else:
            s_count[s[right]] = 1

        if right - left == len(p) - 1:
            if s_count == p_count:
                res.append(left)

            s_count[s[left]] -= 1
            if s_count[s[left]] == 0:
                del s_count[s[left]]
            left += 1

    return res


findAnagrams(s, p)
