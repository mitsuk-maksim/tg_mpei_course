# https://leetcode.com/problems/defanging-an-ip-address/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.',"[.]")






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
            address = stringToString(line);
            
            ret = Solution().defangIPaddr(address)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
