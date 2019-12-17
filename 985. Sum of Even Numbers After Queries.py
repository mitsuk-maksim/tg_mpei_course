# https://leetcode.com/problems/sum-of-even-numbers-after-queries/

class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        sm = sum(x for x in A if x%2 == 0)
        res = []

        for x,k in queries:
            if A[k] % 2 == 0:
                sm -= A[k]
            A[k] += x
            if A[k] % 2 == 0:
                sm += A[k]
            res.append(sm)
        return res
