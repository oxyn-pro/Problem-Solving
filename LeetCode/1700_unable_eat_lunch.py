# TC: O(n)
# SC: O(1) - It is still O(1) since there are only 2 possible sandwich types 0 or 1
def count_students(students, sandwiches):
    """Solved using a hashmap containing sandwich types and their counts"""
    res = len(students)
    st_cnt = {}

    for s in students:
        if s not in st_cnt:
            st_cnt[s] = 0
        st_cnt[s] += 1

    for i in sandwiches:
        if st_cnt[i] > 0:
            res -= 1
            st_cnt[i] -= 1
        else:
            return res
    return res


# TC: O(n)
# SC: O(1)
def count_students_cnts(students, sandwiches):
    """Solved using 2 counter vars"""
    res = len(students)
    st_1 = 0
    st_0 = 0

    for s in students:
        if s:
            st_1 += 1
        else:
            st_0 += 1

    for i in sandwiches:
        if i and st_1 > 0:
            st_1 -= 1
        elif not i and st_0 > 0:
            st_0 -= 1
        else:
            return res
        res -= 1
    return res


# TC: O(n)
# SC: O(n)
def count_students(students, sandwiches):
    """Solved using queue"""
    from collections import deque

    st_q = deque(students)

    for s in sandwiches:
        if s in st_q:
            while s != st_q[0]:
                st = st_q.popleft()
                st_q.append(st)
            st_q.popleft()
        else:
            return len(st_q)
    return 0


students = [1, 1, 1, 0, 0, 1]
sandwiches = [1, 0, 0, 0, 1, 1]

count_students(students, sandwiches)
