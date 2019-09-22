# https://leetcode.com/problems/fibonacci-number/
class Solution:
    def fib(self, N: int) -> int:
        fib1 = 0
        fib2 = 1 
        for i in range (N):
            fib1,fib2 = fib2, fib1+fib2
        return fib1

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
            N = int(line);
            
            ret = Solution().fib(N)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
