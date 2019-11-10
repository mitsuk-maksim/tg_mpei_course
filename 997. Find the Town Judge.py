# https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1:
            return 1
        judge = {}
        count = []
        for pair in trust:
            if pair[0] not in count:
                count.append(pair[0])
            if pair[1] not in judge:
                judge[pair[1]] = 1
            else:
                judge[pair[1]] += 1
        result = max(judge.items(),key = lambda a: a[-1])
      #  print(judge)
        
        if result[1] == len(count):
            flag = 0
            for i in judge.values():
                if i == result[1]:
                    flag += 1
         #   print(flag)
            if flag == 1:
                return result[0]
        return -1
