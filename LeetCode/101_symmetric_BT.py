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
node4 = TreeNode(2)
node5 = TreeNode(3)
node6 = TreeNode(1)

root.left = node1
node1.left = node2
node1.right = node3

root.right = node4
node4.left = node5
node4.right = node6

# This Tree looks like:
#        4
#      /   \
#     2     2
#    / \   / \
#   1  3  3  1


# TC: O(n)
# SC: O(n)
def isSymmetric_rec(root):
    def rec(left, right):
        if not left and not right:
            return True

        if not left or not right:
            return False

        return (
            left.val == right.val
            and rec(left.left, right.right)
            and rec(left.right, right.left)
        )

    return rec(root.left, root.right)


isSymmetric_rec(root)


# TC: O(n)
# SC: O(n)
def isSymmetric_loop(root):
    queue = deque()

    if root:
        queue.append(root.left)
        queue.append(root.right)

    while len(queue) > 0:

        left = queue.popleft()
        right = queue.popleft()

        if not left and not right:
            continue

        if not left or not right:
            return False

        if left.val != right.val:
            return False

        queue.append(left.left)
        queue.append(right.right)

        queue.append(left.right)
        queue.append(right.left)

    return True


isSymmetric_loop(root)
