# https://leetcode.com/problems/rotate-string/

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if B in A+A:
            return len(A) == len(B)
