# https://leetcode.com/problems/convert-bst-to-greater-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        
        def f_convert(node, v_val = 0):
            if node:
                node.val += f_convert(node.right, v_val)
                return f_convert(node.left, node.val)
            else:
                return v_val
        
        f_convert(root)
        
        return root
