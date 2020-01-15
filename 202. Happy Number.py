# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, num: int) -> bool:
        s_calculate = set()
        while num != 1:
            if num in s_calculate:
                return False
            s_calculate.add(num)
            num = sum([int(numer)**2 for numer in str(num)])
        return True
