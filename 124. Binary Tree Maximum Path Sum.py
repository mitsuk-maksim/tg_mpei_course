# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def max_help(node):
            if not node:
                return 0
            left = max_help(node.left)
            right = max_help(node.right)
            self.max = max(self.max, left + node.val + right)
            return max(node.val + max(left,right),0)
        self.max = -float('inf') # global
        max_help(root)
      #  print(max_help(root))
        return self.max
