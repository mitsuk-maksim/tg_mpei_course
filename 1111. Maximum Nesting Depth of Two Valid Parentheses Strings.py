# https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/ 

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        res = []
        lvl = -1
        for c in seq:
            if c == '(':
                lvl += 1
                res.append(lvl % 2)
            elif c == ')':
                res.append(lvl % 2)
                lvl -= 1
        return res
