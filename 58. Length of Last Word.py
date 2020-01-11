# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        b = s.split()
        if len(b) == 0:
            return 0
        return len(b[-1])
