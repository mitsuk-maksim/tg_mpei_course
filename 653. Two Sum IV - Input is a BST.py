# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        l_bfs = [root]
        s_set = set()
        for num in l_bfs:
            if (k - num.val) in s_set:
                return True
            s_set.add(num.val)
            if num.left:
                l_bfs.append(num.left)
            if num.right:
                l_bfs.append(num.right)
        return False
