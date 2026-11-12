class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        if len(prices) == 1:
            return 0
        
        curBuy = prices[left]
        maxProfit = 0
        
        for right in range(1, len(prices)):
            if prices[right] > prices[left]:
                maxProfit = max(maxProfit, prices[right] - prices[left])
            elif prices[right] < prices[left]:
                left = right
        
        return maxProfit



        