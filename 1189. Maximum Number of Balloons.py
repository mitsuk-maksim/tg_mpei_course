# https://leetcode.com/problems/maximum-number-of-balloons/

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        return min(text.count(char) // int(c_int) for char, c_int in zip("balon","11221"))
