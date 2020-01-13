# https://leetcode.com/problems/occurrences-after-bigram/

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        char = text.split()
        result = []

        for i in range(2,len(char)):
            if char[i-2] == first and char[i-1] == second:
                result.append(char[i])

        return result
