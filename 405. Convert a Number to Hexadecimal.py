# https://leetcode.com/problems/convert-a-number-to-hexadecimal/

class Solution:
    def toHex(self, num: int) -> str:
        if num < 0:
            num += 2**32
        result_stack = []
        q = "0123456789abcdef"
        
        while num:
            result_stack.append(q[num%16])
            num //= 16
        
        if not result_stack:
            return '0'
        
        result_stack.reverse()
        return "".join(result_stack)
