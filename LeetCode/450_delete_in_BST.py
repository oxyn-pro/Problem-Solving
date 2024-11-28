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
def delete_node_rec(root, key):
    if not root:
        return

    if key < root.val:
        root.left = delete_node_rec(root.left, key)
    elif key > root.val:
        root.right = delete_node_rec(root.right, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            min_node = find_min_node_rec(root.right)
            root.val = min_node.val
            root.right = delete_node_rec(root.right, min_node.val)
    return root


def find_min_node_rec(root):
    if not root.left:
        return root

    return find_min_node_rec(root.left)


# delete_node_rec(root, 2)


# TC: O(n) - If it is Unbalanced, but on average it is Balanced and that's why it is O(log n)
# SC: O(1)
def delete_node_loop(root, key):
    curr_root = root
    parent = None

    # Example: If we need to delete 2, after this loop curr_root = 2, parent = 4
    while curr_root and curr_root.val != key:
        parent = curr_root
        if key < curr_root.val:
            curr_root = curr_root.left
        elif key > curr_root.val:
            curr_root = curr_root.right

    if not curr_root:
        return root

    # Example: If we need to remove 1, then this Tree will look like this
    # after the first if (second if will not even execute):
    #       4
    #      / \
    #     2   7
    #      \
    #      3
    if not curr_root.left or not curr_root.right:
        child = curr_root.right if not curr_root.left else curr_root.left

        if not parent:
            return child

        if parent.left == curr_root:
            parent.left = child
        else:
            parent.right = child

    # Example: If we need to remove 4, then this Tree will look like this after the second if:
    #       7
    #      /
    #     2
    #    / \
    #   1  3
    else:
        # Find the minimum node on the right side of the tree
        min_node, min_node_parent = find_min_node_loop(curr_root.right, curr_root)
        curr_root.val = min_node.val

        if not min_node.left or not min_node.right:
            min_node_child = min_node.right if not min_node.left else min_node.left

            if min_node_parent.left == min_node:
                min_node_parent.left = min_node_child
            else:
                min_node_parent.right = min_node_child

    return root


def find_min_node_loop(root, min_node_parent):
    while root.left:
        min_node_parent = root
        root = root.left

    return root, min_node_parent


delete_node_loop(root, 4)
