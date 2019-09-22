# https://leetcode.com/problems/hamming-distance/
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        mas_bin_x = [0]*32
        mas_bin_y = [0]*32
        mas_bin_x = list(bin(x)[2:])
        mas_bin_y = list(bin(y)[2:])
        for i in range(len(mas_bin_x),32):
               mas_bin_x.insert(0,'0')
        for i in range(len(mas_bin_y),32):
               mas_bin_y.insert(0,'0')
        count = 0
        for i in range(32):
            if mas_bin_x[i] != mas_bin_y[i]:
                count+=1
        return count

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
            line = next(lines)
            y = int(line);
            
            ret = Solution().hammingDistance(x, y)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
