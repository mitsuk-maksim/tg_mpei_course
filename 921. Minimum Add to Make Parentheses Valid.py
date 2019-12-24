# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        for char in S:
            if char == '(' or len(stack) == 0:
                stack.append(char)
            else:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(char)
        return len(stack)
