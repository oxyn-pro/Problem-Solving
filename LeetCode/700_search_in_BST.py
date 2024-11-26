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
def searchBST_rec(root, val):
    if not root:
        return

    if root.val > val:
        return searchBST_rec(root.left, val)
    elif root.val < val:
        return searchBST_rec(root.right, val)
    else:
        return root


print(searchBST_rec(root, 2).val)


# TC: O(n) - If it is Unbalanced, but on average it is Balanced and that's why it is O(log n)
# SC: O(1)
def searchBST_loop(root, val):
    while root:
        if root.val > val:
            root = root.left
        elif root.val < val:
            root = root.right
        else:
            return root

    return


print(searchBST_loop(root, 2).val)
