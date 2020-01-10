# https://leetcode.com/problems/valid-mountain-array/

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        v_length = len(A)
        i = 0
        while i+1 < v_length and A[i] < A[i+1]: # идем до пика
            i += 1
        
        #убеждаемся что он не первый и не последний
        if i != 0 and i != v_length-1:
            while i+1 < v_length and A[i] > A[i+1]:
                i += 1
            
            return i == v_length - 1
        return False
