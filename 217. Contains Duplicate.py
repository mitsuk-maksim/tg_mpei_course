#https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
  #      print(len(nums),len(set(nums)))
        if len(nums) == len(set(nums)):
            return False
        else:
            return True
