# https://leetcode.com/problems/detect-capital/

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count = 0
        for char in word:
            if char == char.upper():
                count += 1
        return (len(word) == count
        or (count == 1 and word[0] == word[0].upper()) or count == 0)
