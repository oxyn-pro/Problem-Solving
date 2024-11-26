class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(6)
node1 = TreeNode(2)
node2 = TreeNode(0)
node3 = TreeNode(4)
node4 = TreeNode(3)
node5 = TreeNode(5)
node6 = TreeNode(8)
node7 = TreeNode(7)
node8 = TreeNode(9)

root.left = node1
node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5

root.right = node6
node6.left = node7
node6.right = node8

# This Tree looks like:
#        6
#      /   \
#     2     8
#    / \   / \
#   0  4  7  9
#     / \
#    3  5


def LCA_BST_rec(root, p, q):
    if not root:
        return

    if p.val > root.val and q.val > root.val:
        return LCA_BST_rec(root.right, p, q)
    elif p.val < root.val and q.val < root.val:
        return LCA_BST_rec(root.left, p, q)
    else:
        return root


print(LCA_BST_rec(root, node1, node3).val)


def LCA_BST_loop(root, p, q):
    while root:
        if p.val > root.val and q.val > root.val:
            root = root.right
        elif p.val < root.val and q.val < root.val:
            root = root.left
        else:
            return root


print(LCA_BST_loop(root, node1, node3).val)
