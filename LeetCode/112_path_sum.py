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


def hasPathSum(root, targetSum):
    if not root:
        return False
    targetSum -= root.val

    if not root.left and not root.right and targetSum == 0:
        return True

    if hasPathSum(root.left, targetSum):
        return True

    if hasPathSum(root.right, targetSum):
        return True

    return False


print(hasPathSum(root, 9))
