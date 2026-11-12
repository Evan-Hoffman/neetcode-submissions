class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #with 2 ptrs, left and right, set buy price to left
        #move right, check max of max variable and diff
        #if right is smaller than left, we can set left to right

        left = 0

        curMax = 0

        for right in range(1, len(prices)):
            if prices[right] < prices[left]:
                left = right

            else:
                curMax = max(curMax, prices[right] - prices[left])

        return curMax            




























        # left = 0
       
        # maxProfit = 0
        
        # for right in range(1, len(prices)):
        #     if prices[right] > prices[left]:
        #         maxProfit = max(maxProfit, prices[right] - prices[left])
        #     elif prices[right] < prices[left]:
        #         left = right
        
        # return maxProfit



        