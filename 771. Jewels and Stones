class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        n = 0
        for i in J:
            n+=S.count(i)
        return n

def stringToString(input):
    import json

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
            J = stringToString(line);
            line = next(lines)
            S = stringToString(line);
            
            ret = Solution().numJewelsInStones(J, S)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
