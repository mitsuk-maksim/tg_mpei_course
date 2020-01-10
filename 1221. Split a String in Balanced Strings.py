# https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        left_count = right_count = result = 0
        for char in s:
            if char == 'R':
                right_count += 1
            else:
                left_count += 1
            if right_count == left_count:
                result += 1
        return result
