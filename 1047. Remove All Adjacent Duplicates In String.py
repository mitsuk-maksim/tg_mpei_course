# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution:
    def removeDuplicates(self, S: str) -> str:
        res = []
        for char in S:
            if res and res[-1] == char:
                res.pop()
            else:
                res.append(char)
        return "".join(res)
