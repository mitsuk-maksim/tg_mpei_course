# https://leetcode.com/problems/groups-of-special-equivalent-strings/

class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        result = set()
        for char in A:
            char = ''.join(sorted(char[::2]) + sorted(char[1::2]))
            result.add(char)
        return len(result)
