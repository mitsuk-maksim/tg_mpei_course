# https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        flag = False
        result = []
        for str in source:
            i = 0
            if not flag:
                new_str = []
            while i < len(str):
                if not flag and str[i:i+2] =="/*":
                    flag = True
                    i += 1
                elif flag and str[i:i+2] == "*/":
                    flag = False
                    i += 1
                elif not flag and str[i:i+2] == "//":
                    break
                elif not flag:
                    new_str.append(str[i])
                i += 1
            if not flag and new_str:
                result.append("".join(new_str))
        return result
