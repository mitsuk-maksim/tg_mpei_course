# https://leetcode.com/problems/insert-into-a-binary-search-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)

        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)

        return root
