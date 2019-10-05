# https://leetcode.com/problems/fizz-buzz/

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        a = [""]*(n)
        for i in range(1,n+1):
            if i%3 == 0 and i%5 != 0:
                a[i-1] = "Fizz"
            elif i%5 == 0 and i%3 != 0:
                a[i-1] = "Buzz"
            elif i%5 == 0 and i%3 == 0:
                a[i-1] = "FizzBuzz"
            else:
                a[i-1] = str(i)
        return(a)
