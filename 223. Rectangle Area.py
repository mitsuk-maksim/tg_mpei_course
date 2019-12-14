# https://leetcode.com/problems/rectangle-area/

class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        area_1 = abs(C-A)*abs(B-D)
        area_2 = abs(E-G)*abs(F-H)
        width = min(C,G) - max(A,E)
        height = min(D,H) - max(B,F)
        if width <= 0 or height <= 0:
            return area_1 + area_2
        else:
            return area_1 + area_2 - width*height
