# https://leetcode.com/problems/next-permutation/

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Используем два указателя с конца, первый j остановится
        в точке убывания, второй i остановится когда значение > nums[j]
        затем меняем местами и сортируем
        """
        if not nums:
            return None
        i = len(nums) - 1
        j = -1 # например для случая 54321, поэтому потом отмена
        flag = True
        while i>0 and flag:
            if nums[i-1] < nums[i]:
                j = i-1
                flag = False
            if flag:
                i -= 1

        for i in range(len(nums)-1, -1, -1):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                nums[j+1:] = sorted(nums[j+1:])
                return 
