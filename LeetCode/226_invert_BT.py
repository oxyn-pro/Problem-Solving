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
#        4                4
#      /   \            /   \
#     2     7    ->    7     2
#    / \   / \        / \   / \
#   1  3  6  9       9  6  3  1


# TC: O(n)
# SC: O(n)
def invert_tree_DFS_rec(root):
    """Depth First Search - Postorder Traverse"""
    if not root:
        return

    invert_tree_DFS_rec(root.left)
    invert_tree_DFS_rec(root.right)
    root.left, root.right = root.right, root.left

    return root


invert_tree_DFS_rec(root)


# TC: O(n)
# SC: O(n)
def invertTree_BFS(root):
    """Breadth First Search - Inlevel Traverse"""
    queue = deque()

    if root:
        queue.append(root)

    while len(queue) > 0:
        for _ in range(len(queue)):
            curr_root = queue.popleft()
            curr_root.left, curr_root.right = curr_root.right, curr_root.left

            if curr_root.left:
                queue.append(curr_root.left)

            if curr_root.right:
                queue.append(curr_root.right)

    return root
