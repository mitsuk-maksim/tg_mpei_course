# https://leetcode.com/problems/complex-number-multiplication/

class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        #используем формулу
        # (a+ib)×(x+iy)=ax+i^2*by+i(bx+ay)=ax−by+i(bx+ay)
        num1 = a.split('+')
        num1[0] = int(num1[0])
        num1[1] = int(num1[1][:-1])
        
        num2 = b.split('+')
        num2[0] = int(num2[0])
        num2[1] = int(num2[1][:-1])
        
        real = str(num1[0]*num2[0] - num1[1]*num2[1])
        print(real)
        img = str(num1[1]*num2[0] + num1[0]*num2[1]) + 'i'
        print(img)
        result = real + '+' + img
        print(result)
        return result
