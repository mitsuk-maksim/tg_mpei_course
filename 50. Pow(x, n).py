#https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n%2 == 0:
            return (x*x)**(n//2)
        else:
           return x*self.myPow(x,n-1) 
   
