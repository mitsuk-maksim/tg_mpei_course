# https://leetcode.com/problems/self-dividing-numbers/

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for i in range (left, right+1):
            flag = True
            for num in str(i):
                if num == '0':
                    flag = False
                    break
                elif i % int(num) != 0:
                    flag = False
                    break
            if flag:
                result.append(i)
        return result





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
            left = int(line);
            line = next(lines)
            right = int(line);
            
            ret = Solution().selfDividingNumbers(left, right)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
