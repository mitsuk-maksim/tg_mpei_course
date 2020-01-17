# https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s_set = {}
        for i, num in enumerate(nums2):
            for nm in nums2[i+1:]:
                if num < nm:
                    s_set[num] = nm
                    break
        
        return [s_set.get(num,-1) for num in nums1]
