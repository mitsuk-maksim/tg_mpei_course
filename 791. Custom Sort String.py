# https://leetcode.com/problems/custom-sort-string/

class Solution:
    def customSortString(self, S: str, T: str) -> str:
        return "".join(sorted(T, key = lambda char: S.index(char) if char in S else 0))
