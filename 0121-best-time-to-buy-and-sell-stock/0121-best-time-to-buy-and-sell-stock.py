class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mini = prices[0]
        profit = 0
        
        for i in range(1, len(prices)):
            
            if prices[i] < mini:
                mini = prices[i]
                
            if profit < prices[i] - mini:
                profit = prices[i] - mini
        return profit
       