# TC: O(n)
# SC: O(n)
def cal_points(operations):
    st = []
    for op in operations:
        if op == "C":
            st.pop()
        elif op == "D":
            st.append(st[-1] * 2)
        elif op == "+":
            st.append(st[-1] + st[-2])
        else:
            st.append(int(op))

    return sum(st)


operations = ["5", "-2", "4", "C", "D", "9", "+", "+"]
cal_points(operations)
