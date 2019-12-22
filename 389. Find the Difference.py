# https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        answer = 0
        for char in s+t:
            answer ^= ord(char) # используем XOR
        return chr(answer)
