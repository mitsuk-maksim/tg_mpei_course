# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = {}
        for num in arr:
            count[num] = count.get(num, 0) + 1
        return list(dict.keys(count))[list(dict.values(count)).index(max(dict.values(count)))]
