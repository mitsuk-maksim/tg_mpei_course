# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        total_number = m + n - 2
        down_number = m - 1
        # надо вычислить С из total_number по down_number
        return math.factorial(total_number)//(math.factorial(down_number) * math.factorial(total_number - down_number))




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
            m = int(line);
            line = next(lines)
            n = int(line);
            
            ret = Solution().uniquePaths(m, n)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
