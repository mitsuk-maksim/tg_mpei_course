# https://leetcode.com/problems/power-of-three/
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==1:
            return True
        elif n>1:
           flag=True
           while (flag) and (n!=1):
                if n%3==0:
                    n/=3
                else:
                    flag=False
           return(flag)
        else:
            return False

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
            
            ret = Solution().isPowerOfThree(n)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
