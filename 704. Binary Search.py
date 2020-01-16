# https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l_point = 0
        r_point = len(nums) - 1
        while l_point <= r_point:
            point = l_point + (r_point - l_point)//2
            if nums[point] == target:
                return point
            if target < nums[point]:
                r_point = point - 1
            else:
                l_point = point + 1
            
        return -1
