'''
 using memoization Technique efficent for large Numbers
'''

class Solution:
    def fib(self, n: int) -> int:
        memo = {}

        def fibo(n):
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1
            else:
                if n in memo:
                    return memo[n]
                else:
                    x = fibo(n-1) + fibo(n-2)
                    memo[n] = x
                    return memo[n]
        return fibo(n)