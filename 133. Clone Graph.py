# https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        memo = {}
        def clone(node):
            if node not in memo:
                c = memo[node] = Node(node.val, [])
                c.neighbors = list(map(clone,node.neighbors))
            return memo[node]
        return node and clone(node)
