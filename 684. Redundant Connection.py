# https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        s_vis = set()
        s_vis.add(edges[0][0])
        s_vis.add(edges[0][1])
        edges.pop(0)
        l_dup = list()
        i = 0
        while i < len(edges):
            if edges[i][0] in s_vis or edges[i][1] in s_vis:
                if edges[i][0] in s_vis and edges[i][1] in s_vis:
                    l_dup.append(edges[i])
                    edges.pop(i)
                else:
                    s_vis.add(edges[i][0])
                    s_vis.add(edges[i][1])
                    edges.pop(i)
                i = 0
            else:
                i += 1
        return l_dup[-1]
