# https://leetcode.com/problems/degree-of-an-array/

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d_fst, d_count = {}, {}
        result = 0
        v_power = 0 #максимальная cтепень

        for i, num in enumerate(nums):
            d_fst.setdefault(num, i)  # возвращает значение по ключу, если его нет, то добавляет
            d_count[num] = d_count.get(num,0) + 1
            if d_count[num] > v_power:
                v_power = d_count[num]
                result = i - d_fst[num] + 1
            elif d_count[num] == v_power:
                result = min(result, i - d_fst[num] + 1)
        return result
