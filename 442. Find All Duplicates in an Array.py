# https://leetcode.com/problems/find-all-duplicates-in-an-array/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        s_set = set()
        for num in nums:
            if num not in s_set:
                s_set.add(num)
            else:
                result.append(num)
        return result
