class Solution:
    def fib(self, n: int) -> int:
        
        def fibonacci(n):
            if n in dp: return dp[n]

            if n ==0 or n==1: return n

            dp[n] = fibonacci(n-1) + fibonacci(n-2)
            return dp[n]
            
        dp = {}
        return(fibonacci(n))