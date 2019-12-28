# https://leetcode.com/problems/intersection-of-two-arrays/

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s_set1 = set(nums1)
        s_set2 = set(nums2)
        result = []
        for num in s_set1:
            if num in s_set2 and num not in result:
                result.append(num)
        return result
