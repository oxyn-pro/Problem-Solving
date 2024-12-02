from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(4)
node1 = TreeNode(2)
node2 = TreeNode(1)
node3 = TreeNode(3)
node4 = TreeNode(7)
node5 = TreeNode(6)
node6 = TreeNode(9)

root.left = node1
node1.left = node2
node1.right = node3

root.right = node4
node4.left = node5
node4.right = node6

# This Tree looks like:
#        4
#      /   \
#     2     7
#    / \   / \
#   1  3  6  9


# TC: O(n)
# SC: O(n)
def right_side_view(root):
    res = []
    queue = deque()

    if root:
        queue.append(root)

    while len(queue) > 0:
        res.append(queue[-1].val)
        for _ in range(len(queue)):
            curr_root = queue.popleft()

            if curr_root.left:
                queue.append(curr_root.left)
            if curr_root.right:
                queue.append(curr_root.right)

    return res


right_side_view(root)


# TC: O(n)
# SC: O(n)
def right_side_view2(root):
    total = []
    queue = deque()

    if root:
        queue.append(root)

    while len(queue) > 0:
        level = []
        for _ in range(len(queue)):
            curr_root = queue.popleft()
            level.append(curr_root.val)

            if curr_root.left:
                queue.append(curr_root.left)
            if curr_root.right:
                queue.append(curr_root.right)
        total.append(level)

    res = []
    for i in total:
        res.append(i[-1])

    return res


right_side_view2(root)
