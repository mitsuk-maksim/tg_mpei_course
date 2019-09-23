#https://leetcode.com/problems/robot-return-to-origin/

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dictionary = {'R':1,'L':-1,'U':1,'D':-1}
        x,y=0,0
        for i in moves:
            if i == 'R' or i == 'L':
                x += dictionary[i]
            else:
                y += dictionary[i]
        if x==0 and y==0:
            return True
        else:
            return False

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
            moves = stringToString(line);
            
            ret = Solution().judgeCircle(moves)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
