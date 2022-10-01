class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        def is_power_of_four(n):
            if n == 1:
                return True
            elif n < 4 or n%4 !=0:
                return False
            else:
                return is_power_of_four(n/4) 

        return is_power_of_four(n)