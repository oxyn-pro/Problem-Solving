s = "anagram"
t = "nagaram"


# TC: O(n)
# SC:  O(n)
def isAnagram_hmap(s, t):
    hmap1 = {}
    hmap2 = {}
    for i in s:
        if i in hmap1:
            hmap1[i] += 1
        else:
            hmap1[i] = 1

    for i in t:
        if i in hmap2:
            hmap2[i] += 1
        else:
            hmap2[i] = 1

    return hmap1 == hmap2


print(isAnagram_hmap(s, t))


# TC: O(n)
# SC:  O(n)
def isAnagram_hmap2(s, t):
    hmap = {}
    for i in s:
        if i in hmap:
            hmap[i] += 1
        else:
            hmap[i] = 1

    for i in t:
        if i in hmap:
            hmap[i] -= 1
        else:
            return False

    for i in hmap:
        if hmap[i] == 0:
            continue
        else:
            return False

    return True


print(isAnagram_hmap2(s, t))


# TC: O(n log n)
# SC:  O(1)
def isAnagram_hmap3(s, t):
    return sorted(s) == sorted(t)


print(isAnagram_hmap3(s, t))
