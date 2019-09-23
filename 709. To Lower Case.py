#https://leetcode.com/problems/to-lower-case/
class Solution:
    def toLowerCase(self, str: str) -> str:
        upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower_case = "abcdefghijklmnopqrstuvwxyz"
        dictionary = dict(zip(upper_case,lower_case))
        result=""
        for i in str:
            if i in upper_case:
                result+=dictionary[i]
            else:
                result+=i
        return result

def stringToString(input):
    import json

    return json.loads(input)

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            str = stringToString(line);
            
            ret = Solution().toLowerCase(str)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
