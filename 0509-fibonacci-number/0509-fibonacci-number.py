class Solution:
    def fib(self, n: int) -> int:
        dp = [0 for x in range(n+1)]
        dp[0] = 0
        
        if n >= 1:
            dp[1] = 1

            for i in range(2, n+1):
                dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
