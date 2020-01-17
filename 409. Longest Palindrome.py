# https://leetcode.com/problems/longest-palindrome/

import collections
class Solution:
    def longestPalindrome(self, s):
        result = 0
        for char in collections.Counter(s).values():
            result += char//2*2
            if char % 2 == 1 and result % 2 == 0:
                result += 1
                
        return result
            
