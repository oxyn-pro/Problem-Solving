class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]


# TC: O(n^2) - Because slicing creates new subarrays
# SC: O(n^2)- Because slicing creates new subarrays
def bin_tree_rec(preorder, inorder):
    if not preorder or not inorder:
        return

    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])

    root.left = bin_tree_rec(preorder[1 : mid + 1], inorder[:mid])
    root.right = bin_tree_rec(preorder[mid + 1 :], inorder[mid + 1 :])

    return root


bin_tree_rec(preorder, inorder).val


# TC: O(n)
# SC: O(n)
def bin_tree_rec2(preorder, inorder):
    inorder_map = {val: idx for idx, val in enumerate(inorder)}
    preorder_idx = 0

    def tree_rec(s, e):
        nonlocal inorder_map, preorder_idx
        if s > e:
            return

        rt_val = preorder[preorder_idx]
        root = TreeNode(rt_val)
        mid = inorder_map[rt_val]
        preorder_idx += 1

        root.left = tree_rec(s, mid - 1)
        root.right = tree_rec(mid + 1, e)

        return root

    return tree_rec(0, len(inorder) - 1)


bin_tree_rec2(preorder, inorder)
