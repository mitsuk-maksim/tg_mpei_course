# https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        n = len(A)
        result = []
        for i in range(n):
            max_current = max(A[0:n-i])
            j = 0
            while A[j] != max_current:
                j += 1
            # реверсним j+1 элементов
            A[:j+1] = reversed(A[:j+1])
            result.append(j+1)
            # реверс всего
            A[:n-i] = reversed(A[:n-i])
            result.append(n-i)
        return result
