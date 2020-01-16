# https://leetcode.com/problems/1-bit-and-2-bit-characters/

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        ind = 0
        while ind < len(bits)-1:
            ind += bits[ind] + 1
        return ind == len(bits) - 1
