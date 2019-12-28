# https://leetcode.com/problems/rotated-digits/

class Solution:
    def rotatedDigits(self, N: int) -> int:
        v_count = 0
        for i in range(1, N+1):
            v_flag = False
            for char in str(i):
                if char in "2569":
                    v_flag = True
                elif char in "347":
                    v_flag = False
                    break
            if v_flag:
                v_count += 1
        return v_count
