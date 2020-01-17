# https://leetcode.com/problems/delete-columns-to-make-sorted/

class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        result = 0
        for colum in zip(*A):
            for i in range(len(colum)-1):
                if colum[i] > colum[i+1]:
                    result += 1
                    break
          #  if any(colum[i] > colum[i+1] for i in range(len(colum)-1)):
           #     result += 1
        return result
