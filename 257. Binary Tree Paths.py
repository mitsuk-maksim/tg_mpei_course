# https://leetcode.com/problems/binary-tree-paths/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        result = [str(root.val) + "->" + val for val in self.binaryTreePaths(root.left)]
        result += [str(root.val) + "->" + val for val in self.binaryTreePaths(root.right)]
        return result or [str(root.val)] # если пустой вернуть список
