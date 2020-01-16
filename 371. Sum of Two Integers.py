# https://leetcode.com/problems/sum-of-two-integers/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b:
            calculate = a^b
            b = (a&b) << 1
            a = calculate & 0xffffffff
        if a >> 31 == 0:
            return a
        return ~(a^0xffffffff)
