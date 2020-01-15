# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = 0
        for i in range(len(digits)):
            result = result*10 + digits[i]
        return [int(i) for i in str(result+1)]



