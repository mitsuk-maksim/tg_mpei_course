# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        result = []
        
        def input(root):
            if root:
                input(root.left)
                result.append(root.val)
                input(root.right)
        
        input(root1)
        input(root2)
        result.sort()
        return result
