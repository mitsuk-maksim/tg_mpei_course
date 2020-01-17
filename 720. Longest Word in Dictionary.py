# https://leetcode.com/problems/longest-word-in-dictionary/

class Solution:
    def longestWord(self, words: List[str]) -> str:
        result = ""
        set_word = set(words)
        for char in words:
            if len(char) > len(result) or char < result and len(char) == len(result) :
                if all(char[:i] in set_word for i in range(1,len(char))):
                    result = char
                    
        return result
