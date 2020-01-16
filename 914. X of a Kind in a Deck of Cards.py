# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        import collections
        result = collections.Counter(deck)
        n = len(deck)
        for i in range(2,n+1):
            if n%i == 0:
                if all(val%i == 0 for val in result.values()):
                    return True
        return False
