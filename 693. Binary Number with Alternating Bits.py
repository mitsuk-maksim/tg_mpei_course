# https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        string = str(bin(n))[2:]
        for i in range (1,len(string)):
            if string[i] == string[i-1]:
                return False
        return True
