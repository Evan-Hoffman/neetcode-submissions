class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        numSet = set(nums)

        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                curLen = 1

                nextNum = num + 1

                while nextNum in numSet:
                    curLen += 1
                    nextNum += 1
                
                longest = max(longest, curLen)
            
        
        return longest





        
        