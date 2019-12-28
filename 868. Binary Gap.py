# https://leetcode.com/problems/binary-gap/

class Solution:
    def binaryGap(self, N: int) -> int:
        v_prev = 0
        v_distant = 0
        for i, num in enumerate(bin(N)[2:]):
            if num == '1':
                v_distant = max(v_distant, i - v_prev)
                v_prev = i
        return v_distant
