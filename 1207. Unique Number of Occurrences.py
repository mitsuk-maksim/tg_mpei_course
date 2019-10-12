# https://leetcode.com/problems/unique-number-of-occurrences/

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict_arr = dict.fromkeys(arr,0)
        for num in arr:
            dict_arr[num] += 1
        if len(dict_arr.values()) == len(set(dict_arr.values())):
            return True
        else:
            return False






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
            arr = stringToIntegerList(line);
            
            ret = Solution().uniqueOccurrences(arr)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
