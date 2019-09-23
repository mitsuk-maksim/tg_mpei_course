#https://leetcode.com/problems/power-of-four/submissions/
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num==1:
            return True
        elif num>1:
           flag=True
           while (flag) and (num!=1):
                if num%4==0:
                    num/=4
                else:
                    flag=False
           return(flag)
        else:
            return False
        
