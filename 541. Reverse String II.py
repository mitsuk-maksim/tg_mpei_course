# https://leetcode.com/problems/reverse-string-ii/

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l_s = list(s)
        for i in range(0, len(l_s),2*k):
            l_s[i:i+k] = l_s[i:i+k][::-1]
        return "".join(l_s)
