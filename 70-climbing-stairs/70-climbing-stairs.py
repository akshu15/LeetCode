class Solution:
    def climbStairs(self, n: int) -> int:
        
        def fib(n):
            
            if n in dp: return dp[n]
            
            if n==0 or n==1:
                return 1
            
            dp[n] = fib(n-1) + fib(n-2)
            return dp[n]
            
        dp = {}
        return fib(n)
        
        