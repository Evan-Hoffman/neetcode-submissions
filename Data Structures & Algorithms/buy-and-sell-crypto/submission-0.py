class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## starting at the front, use 2 ptrs, set a max of 0
        ## if val at ptr2 is less than val at ptr1, set ptr1 to ptr2
        ## if val at ptr2 is greater than ptr1, check the profit, update max accordingly
        ## incremement ptr2

        if len(prices) == 1:
            return 0

        ptr1, ptr2 = 0, 1

        curMax = 0

        while ptr2 < len(prices):
            if prices[ptr2] <= prices[ptr1]:
                ptr1 = ptr2
                ptr2 += 1
            elif prices[ptr2] > prices[ptr1]:
                curMax = max(curMax, prices[ptr2] - prices[ptr1])
                ptr2 += 1
        
        return curMax


        