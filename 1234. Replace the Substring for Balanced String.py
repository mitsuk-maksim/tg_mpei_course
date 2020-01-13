# https://leetcode.com/problems/replace-the-substring-for-balanced-string/

import collections
class Solution:
    def balancedString(self, s: str) -> int:
        diction = collections.Counter(s)
        result = len(s)
        point = len(s)
        i = 0
        for j, char in enumerate(s):
            diction[char] -= 1
            while i < point and all(point/4 >= diction[q] for q in "QWER"):
                result = min(result, j-i+1)
                diction[s[i]] += 1
                i += 1
        return result
