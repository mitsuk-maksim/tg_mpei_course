# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for char in letters:
            if char > target:
                return char
        # если этого эл-та нет
        return letters[0]
