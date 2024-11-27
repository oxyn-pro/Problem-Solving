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


# TC: O(n) - If it is Unbalanced, but on average it is Balanced and that's why it is O(log n)
# SC: O(n) - If it is Unbalanced, but on average the call stack of a Balanced BST is O(log n)
def insertIntoBST_rec(root, val):
    if not root:
        return TreeNode(val)

    if val > root.val:
        root.right = insertIntoBST_rec(root.right, val)
    elif val < root.val:
        root.left = insertIntoBST_rec(root.left, val)

    return root


insertIntoBST_rec(root, 5)


# TC: O(n) - If it is Unbalanced, but on average it is Balanced and that's why it is O(log n)
# SC: O(1)
def insertIntoBST_loop(root, val):
    if not root:
        return TreeNode(val)

    curr_root = root
    while curr_root:
        if val > curr_root.val:
            if not curr_root.right:
                curr_root.right = TreeNode(val)
            curr_root = curr_root.right
        elif val < curr_root.val:
            if not curr_root.left:
                curr_root.left = TreeNode(val)
            curr_root = curr_root.left
        else:
            break

    return root


insertIntoBST_loop(root, 5)
