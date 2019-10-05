# https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, b: List[List[int]]) -> List[List[int]]:
            
        m = len(b[0])
        n = len(b)
        a = [[0] * n for i in range (m)]
        
        for i in range(m):
            for j in range(n):
                if i != j:
                    a[i][j] = b[j][i]
                else:
                    a[i][j] = b[i][j]
        
        return a

        
