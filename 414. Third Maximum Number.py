# https://leetcode.com/problems/third-maximum-number/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        result = list(set(nums))
        result.sort()
        if len(result) <= 2:
            return result[-1]
        return result[-3]
