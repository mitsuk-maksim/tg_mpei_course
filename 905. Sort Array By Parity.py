#https://leetcode.com/problems/sort-array-by-parity/

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        A.sort(key = lambda c: c%2)
        return A
