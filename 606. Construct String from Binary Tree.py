# https://leetcode.com/problems/construct-string-from-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ''
       # print(t.val)
      #  print(str(t.val))
        if not t.left and not t.right:
            return str(t.val) + ''
        if not t.right:
            return str(t.val) + '(' + self.tree2str(t.left) + ')'
        #print(type(t.val))
        return str(t.val) + '(' + self.tree2str(t.left) + ")(" + self.tree2str(t.right) + ')'
