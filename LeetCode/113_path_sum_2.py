class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(5)
node1 = TreeNode(4)
node2 = TreeNode(11)
node3 = TreeNode(7)
node4 = TreeNode(2)
node5 = TreeNode(8)
node6 = TreeNode(13)
node7 = TreeNode(4)
node8 = TreeNode(5)
node9 = TreeNode(1)

root.left = node1
node1.left = node2
node2.left = node3
node2.right = node4

root.right = node5
node5.left = node6
node5.right = node7
node7.left = node8
node7.right = node9

# This Tree looks like:
#         5
#       /   \
#      4     8
#     /    /  \
#    11   13   4
#   /  \      / \
#  7   2     5  1


# TC: O(2^n)
# SC: O(2^n)
def pathSum(root, targetSum):
    res = []
    path = []
    cur_sum = 0

    def dfs(root, cur_sum, path):
        if not root:
            return

        path.append(root.val)
        cur_sum += root.val

        if not root.left and not root.right and cur_sum == targetSum:
            res.append(path.copy())
            path.pop()
            cur_sum -= root.val
            return

        dfs(root.left, cur_sum, path)
        dfs(root.right, cur_sum, path)

        path.pop()
        cur_sum -= root.val

    dfs(root, cur_sum, path)
    return res


print(pathSum(root, 22))
