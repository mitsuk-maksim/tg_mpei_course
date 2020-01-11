# https://leetcode.com/problems/valid-palindrome-ii/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        lft_point = 0
        rt_point = len(s) - 1
        while lft_point < rt_point:
            if s[lft_point] != s[rt_point]:
                substr_1 = s[lft_point : rt_point]
                substr_2 = s[lft_point+1 : rt_point+1]
                return substr_1 == substr_1[::-1] or substr_2 == substr_2[::-1]
            lft_point += 1
            rt_point -= 1
        return True
