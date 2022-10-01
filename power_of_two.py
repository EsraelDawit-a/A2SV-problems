from math import log
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <=0: 
            return False
        else:
            return 3**(round(log(n,3))) == n
       
       


       '''
       or using recursion
       '''

       def is_power_of_two(n):
           if n == 1:
             return True
           elif n < 3 or n%3 != 0 :
              return False
           else:
             return is_power_of_two(n/3)
              
