# https://leetcode.com/problems/add-digits/

class Solution:
    def addDigits(self, num: int) -> int:
        flag = True
        i = 0
        while flag:
            if num > 9:
                sm = 0
                for i in str(num):
                    sm += int(i)
                num = sm
            else:
                flag = False
        return num






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
            num = int(line);
            
            ret = Solution().addDigits(num)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
