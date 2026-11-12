class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        longest = 0

        for num in nums:
            if num - 1 not in numSet:
                counter = 1
                while num + counter in numSet:
                    counter += 1
                longest = max(longest, counter)
        
        return longest





        
        