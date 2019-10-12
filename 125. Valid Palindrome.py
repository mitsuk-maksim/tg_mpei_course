# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphab = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        mas_s = []
        mas_s_2=[]
        for i in s:
            if i in alphab:
                mas_s.append(i.lower())
        mas_s_2 = mas_s.copy()
        mas_s_2.reverse()
        if mas_s == mas_s_2:
            return True
        else:
            return False









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
            
            ret = Solution().isPalindrome(s)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
