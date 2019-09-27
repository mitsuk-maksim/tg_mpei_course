# https://leetcode.com/problems/permutation-sequence/
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        k -= 1
        num = [str(i) for i in range(1,n+1)]
        string = ""
        for i in range(1,n):
            f = math.factorial(n-i)
            index = k // f
            string += num.pop(index)
            k %= f
            if k == 0:
                break
        return string + "".join(num)

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
            n = int(line);
            line = next(lines)
            k = int(line);
            
            ret = Solution().getPermutation(n, k)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
