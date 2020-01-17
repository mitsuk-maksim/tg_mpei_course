# https://leetcode.com/problems/number-of-lines-to-write-string/

class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        v_width = 0
        v_line = 1
        for char in S:
            test1 = ord(char)
            test2 = ord('a')
            test = test1 - test2
            v_len = widths[ord(char) - ord('a')]
            v_width += v_len
            if v_width > 100:
                v_width = v_len
                v_line += 1

        return v_line,v_width
