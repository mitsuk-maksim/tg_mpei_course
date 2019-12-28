# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        d_roman_int = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        v_prev = 0
        v_sum = 0
        for i in s[::-1]: # идем с конца
            current_int = d_roman_int[i]
            if v_prev > current_int:
                v_sum -= current_int
            else:
                v_sum += current_int
            v_prev = current_int
        return v_sum
