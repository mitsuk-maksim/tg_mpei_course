# https://leetcode.com/problems/multiply-strings/
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        i_num1,i_num2=0,0
        n1=len(num1)
        n2=len(num2)
        for i in range(1,n1+1):
            i_num1+=int(num1[i-1])*(10**(n1-i))
        for i in range(1,n2+1):
            i_num2+=int(num2[i-1])*(10**(n2-i))
        return str(i_num1*i_num2)

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
            num1 = stringToString(line);
            line = next(lines)
            num2 = stringToString(line);
            
            ret = Solution().multiply(num1, num2)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
