# https://leetcode.com/problems/smallest-range-i/

class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        small = min(A)
        big = max(A)
        difference = big - small
        if difference <= 2*K:
            return 0 # увеличим до k и уменьшим до k, так что все цифры будут равны
        else:
            return difference - 2*K
