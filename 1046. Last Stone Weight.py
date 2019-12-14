# https://leetcode.com/problems/last-stone-weight/

import heapq # модуль для работы с кучами
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1*i for i in stones]
        while len(stones) > 1:
            heapq.heapify(stones) # список в кучу
            s1 = heapq.heappop(stones) # берем элемент c наивысшим весом (со знаком минус)
            s2 = heapq.heappop(stones)
            delta = s1 - s2
            if delta != 0:
                heapq.heappush(stones, delta) # добавление элемента (delta) в кучу (stones)
        if stones:
            return -1*stones[0]
        else:
            return 0
