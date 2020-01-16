# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/

class Solution:
    def largestSumAfterKNegations(self, A:List[int], K: int) -> int:
        import heapq
        # используем кучу
        heapq.heapify(A)
        while K:
            heapq.heapreplace(A, -A[0]) #берем и заменяем минимальный элемент в A на минимальный (A[0]) 
            K -= 1
        return sum(A)
