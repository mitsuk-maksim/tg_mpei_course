# https://leetcode.com/problems/kth-largest-element-in-an-array/


import heapq # модуль для работы с кучами
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-1*i for i in nums]
        heapq.heapify(nums)
        for i in range(k-1):
            heapq.heappop(nums)
        return -1*heapq.heappop(nums)
