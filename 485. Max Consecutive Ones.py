# https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        str_nums = ''.join(map(str, nums))
        mas = str_nums.split('0')
        return len(max(mas))
