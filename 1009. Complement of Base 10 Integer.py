# https://leetcode.com/problems/complement-of-base-10-integer/

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        comp_bin_n = ""
        bin_n = bin(N)[2:]
        
        for i in bin_n:
            if i == '0':
                comp_bin_n += '1'
            else:
                comp_bin_n += '0'
                
        return int((comp_bin_n),2)





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
            
            ret = Solution().bitwiseComplement(N)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
