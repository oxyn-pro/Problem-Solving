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
def inorder_traversal_rec(root):
    ls = []

    def inorder_rec(root):
        if not root:
            return

        inorder_rec(root.left)
        ls.append(root.val)
        inorder_rec(root.right)

    inorder_rec(root)
    return ls


inorder_traversal_rec(root)


# TC: O(n)
# SC: O(n)
def inorder_traversal_loop(root):
    ls = []
    stack = []
    curr_root = root

    while curr_root or stack:
        while curr_root:
            stack.append(curr_root)
            curr_root = curr_root.left
        curr_root = stack.pop()
        ls.append(curr_root.val)
        curr_root = curr_root.right

    return ls


inorder_traversal_loop(root)
