# https://leetcode.com/problems/sort-array-by-parity-ii/
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        result = [0]*len(A)
        i = 0
        j = 1
        for num in A:
            if num%2 == 0:
                result[i] = num
                i+=2
            else:
                result[j] = num
                j+=2
        return result




def stringToIntegerList(input):
    return json.loads(input)

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])

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
            
            ret = Solution().sortArrayByParityII(A)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
