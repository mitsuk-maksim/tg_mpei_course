# https://leetcode.com/problems/n-ary-tree-level-order-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = []
        if root:
            queue = [root]
        else:
            queue = []

        while queue:
            result.append([node.val for node in queue])
            queue = [chld for node in queue for chld in node.children]
        
        return result
