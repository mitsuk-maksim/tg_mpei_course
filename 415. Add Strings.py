# https://leetcode.com/problems/reverse-string-ii/

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        return s[k-1::-1]+s[k::]

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
            s = stringToString(line);
            line = next(lines)
            k = int(line);
            
            ret = Solution().reverseStr(s, k)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
