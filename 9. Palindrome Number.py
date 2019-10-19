# https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            st=str(x)
            if st==st[::-1]:
                return True
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
            x = int(line);
            
            ret = Solution().isPalindrome(x)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
