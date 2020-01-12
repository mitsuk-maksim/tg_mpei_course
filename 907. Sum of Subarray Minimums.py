# https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        A = [0] + A
        l_stack = [0]
        l_sm = [0]*len(A)
        for i in range(len(A)):
            while A[l_stack[-1]] > A[i]:
                l_stack.pop()
            v_k = l_stack[-1]
            l_sm[i] = l_sm[v_k] + (i-v_k)*A[i]
            l_stack.append(i)
        return sum(l_sm) % (10**9 + 7)
