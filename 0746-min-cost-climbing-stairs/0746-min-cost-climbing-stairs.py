class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        len_cost = len(cost)
        dp = [0] * len_cost
        
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2, len_cost):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return min(dp[len_cost - 1], dp[len_cost - 2])