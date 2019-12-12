# https://leetcode.com/problems/leaf-similar-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def f_search(self,root):
        if not root:
            return []
        if not(root.left or root.right):
            return [root.val]
        return self.f_search(root.left) + self.f_search(root.right)

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.f_search(root1) == self.f_search(root2)
