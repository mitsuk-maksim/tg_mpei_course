# https://leetcode.com/problems/toeplitz-matrix/

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        s_groups = {}
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if i-j not in s_groups:
                    s_groups[i-j] = val
                elif s_groups[i-j] != val:
                    return False
        return True
