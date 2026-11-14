class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        curMax = 0

        asSet = set(nums)

        for num in nums:
            if num - 1 not in asSet:
                streak = 1
                while num + streak in asSet:
                    streak += 1
                
                curMax = max(curMax, streak)
        
        return curMax
            


        