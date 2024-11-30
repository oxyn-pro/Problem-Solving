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

root.left = node1
node1.left = node2
node1.right = node3

root.right = node4

# This Tree looks like:
#       4
#      / \
#     2   7
#    / \
#   1  3


# TC: O(n)
# SC: O(n)
def kthSmallest_rec(root, k):
    idx = 0
    ans = None

    def inorder(root):
        nonlocal ans, idx
        if not root:
            return

        inorder(root.left)
        idx += 1
        if idx == k:
            ans = root.val
            return
        inorder(root.right)

    inorder(root)
    return ans


kthSmallest_rec(root, 3)


# TC: O(n)
# SC: O(n)
def kthSmallest_loop(root, k):
    idx = 0
    stack = []
    curr_root = root

    while curr_root or stack:
        while curr_root:
            stack.append(curr_root)
            curr_root = curr_root.left

        curr_root = stack.pop()
        idx += 1
        if idx == k:
            return curr_root.val
        curr_root = curr_root.right


kthSmallest_loop(root, 3)
