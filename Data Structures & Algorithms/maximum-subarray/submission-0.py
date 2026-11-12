class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curMax = float("-inf")

        temp = 0

        for num in nums:
            temp = max(temp + num, num)
            curMax = max(curMax, temp)
        
        return curMax
        