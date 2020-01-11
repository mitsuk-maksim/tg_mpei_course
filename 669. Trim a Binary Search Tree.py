# https://leetcode.com/problems/trim-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
    # def __init__(self, x):
    #     self.val = x
    #     self.left = None
    #     self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        def f_search(node):
            if not node:
                return  None
            elif node.val > R:
                return f_search(node.left)
            elif node.val < L:
                return f_search(node.right)
            else:
                node.right = f_search(node.right)
                node.left = f_search(node.left)
                return node
        return f_search(root)
