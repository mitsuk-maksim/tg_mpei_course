# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        v_rd = 0
        v_wht = 0
        v_bl = len(nums) - 1

        while v_wht <= v_bl:
            if nums[v_wht] == 0:
                nums[v_rd], nums[v_wht] = nums[v_wht], nums[v_rd]
                v_wht += 1
                v_rd += 1
            elif nums[v_wht] == 1:
                v_wht += 1
            else:
                nums[v_wht], nums[v_bl] = nums[v_bl], nums[v_wht]
                v_bl -= 1
