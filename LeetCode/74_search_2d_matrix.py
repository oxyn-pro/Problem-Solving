# TC: O(log n) - Theoretically, it is O(log m + log n), we can simply shorten it to O(log n)
# SC: O(1)
def search_matrix(matrix, target):
    """Use 2 Binary searches. One for the row and two for the elements within that row"""
    m_l = 0
    m_r = len(matrix) - 1

    while m_l <= m_r:
        middle = (m_l + m_r) // 2

        if target < matrix[middle][0]:
            m_r = middle - 1
        elif target > matrix[middle][-1]:
            m_l = middle + 1
        else:
            row_idx = middle
            break
    else:
        return False

    row = matrix[row_idx]
    c_l = 0
    c_r = len(row) - 1

    while c_l <= c_r:
        middle = (c_l + c_r) // 2

        if target < row[middle]:
            c_r = middle - 1
        elif target > row[middle]:
            c_l = middle + 1
        else:
            return True

    return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
search_matrix(matrix, target)
