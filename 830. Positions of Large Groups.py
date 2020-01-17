# https://leetcode.com/problems/positions-of-large-groups/

class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        # два указателя
        i = 0
        l_result = []
        n = len(S)
        for j in range(n):
            if j == n - 1 or S[j] != S[j+1]:
                if j - i + 1 >= 3:
                    l_result.append([i,j])
                i = j + 1
        
        return l_result
