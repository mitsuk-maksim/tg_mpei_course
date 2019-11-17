# https://leetcode.com/problems/minimum-absolute-difference/

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_difference = abs(arr[1] - arr[0])
        for i in range(len(arr) - 1):
            if abs(arr[i+1] - arr[i]) < min_difference:
                min_difference = abs(arr[i+1] - arr[i])
        result = []
        for i in range(len(arr)-1):
            if abs(arr[i+1] - arr[i]) == min_difference:
                result.append([arr[i],arr[i+1]])
        return result

