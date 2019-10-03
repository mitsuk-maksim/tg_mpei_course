# https://leetcode.com/problems/reverse-words-in-a-string-iii/
class Solution:
    def reverseWords(self, s: str) -> str:
        b=s.split(" ")
        for i in range(len(b)):
              b[i] = b[i][::-1]

        return ' '.join(b)





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
            
            ret = Solution().reverseWords(s)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
