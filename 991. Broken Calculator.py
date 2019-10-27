# https://leetcode.com/problems/broken-calculator/

class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        result = 0
        while Y > X:
            result += 1
            if Y%2 != 0:
                Y += 1
            else:
                Y //= 2
        return result + X-Y



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
            X = int(line);
            line = next(lines)
            Y = int(line);
            
            ret = Solution().brokenCalc(X, Y)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
