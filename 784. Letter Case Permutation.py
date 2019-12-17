# https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = [S]
        for i,ch in enumerate(S):
            if ch.isalpha():
                res.extend([s[:i] + s[i].swapcase() + s[i+1:] for s in res])
        return res
