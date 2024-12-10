from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)

root2 = TreeNode(1)
node3 = TreeNode(2)
node4 = TreeNode(3)


root.left = node1
root.right = node2

root2.left = node3
root2.right = node4

# This Tree looks like:
#        1                1
#      /   \            /   \
#     2     3          2     3


# TC: O(n)
# SC: O(n)
def isSameTree_dfs(p, q):
    if not p and not q:
        return True

    if not p or not q:
        return False

    return (
        p.val == q.val
        and isSameTree_dfs(p.left, q.left)
        and isSameTree_dfs(p.right, q.right)
    )


isSameTree_dfs(root, root2)


# TC: O(n)
# SC: O(n)
def isSameTree_bfs(p, q):
    queue = deque()
    queue.append(p)
    queue.append(q)

    while len(queue) > 0:
        p = queue.popleft()
        q = queue.popleft()

        if not p and not q:
            continue

        if not p or not q:
            return False

        if not p.val == q.val:
            return False

        queue.append(p.left)
        queue.append(q.left)

        queue.append(p.right)
        queue.append(q.right)

    return True


isSameTree_bfs(root, root2)
