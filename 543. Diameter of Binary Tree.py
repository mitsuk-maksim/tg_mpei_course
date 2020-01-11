# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.result = 0
        def search(node):
            if not node:
                return 0
            left, right = search(node.left), search(node.right)
            self.result = max(self.result, left+right)
            return 1 + max(left,right)
        search(root)
        return self.result
