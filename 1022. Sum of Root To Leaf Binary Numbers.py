# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def check(root, result):
            if not root:
                return 0
            result = result * 2 + root.val
            if root.left == root.right:
                return result
            return check(root.left, result) + check(root.right, result)
        return check(root,0)
