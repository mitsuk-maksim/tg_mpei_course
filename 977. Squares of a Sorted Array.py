#https://leetcode.com/problems/squares-of-a-sorted-array/
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:

        b=[i*i for i in A]
        b.sort()
        return b
            
        
