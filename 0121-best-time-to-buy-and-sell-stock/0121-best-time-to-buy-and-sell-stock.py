class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        base = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if base > prices[i]:
                base = prices[i]
            
            if prices[i] - base > profit:
                profit = prices[i] - base
        return profit