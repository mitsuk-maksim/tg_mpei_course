# https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        return A.index(max(A))





def stringToIntegerList(input):
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
            A = stringToIntegerList(line);
            
            ret = Solution().peakIndexInMountainArray(A)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
