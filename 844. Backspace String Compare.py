# https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def construct_str(self,string):
        result = []
        for char in string:
            if char != '#':
                result.append(char)
            elif result:
                result.pop()
        return "".join(result)
    
    
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.construct_str(S) == self.construct_str(T)
