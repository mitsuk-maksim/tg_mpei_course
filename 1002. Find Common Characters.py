# https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        result = []
        for char in A[0]:
            print(char)
            flag = True
            for i in range (1,len(A)):
               # print(A[i])
               # print(result)
                position = A[i].find(char)
                if position == -1:
                    flag = False
                    break
                else:
                    A[i] = A[i][:position] + A[i][position+1:]
            if flag:
                result.append(str(char))
        return result

