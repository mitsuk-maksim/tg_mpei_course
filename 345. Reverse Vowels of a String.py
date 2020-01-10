# https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution:
    def reverseVowels(self, s: str) -> str:
        glasn = "euioaEUIOA"
        s2 = []
        for ch in s:
            if ch in glasn:
                s2.append(ch)
                
        result = ""
        for ch in s:
            if ch in glasn:
                result += s2.pop()
            else:
                result += ch
        return result
            
