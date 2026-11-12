class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        curMax = 0

        for num in nums:
            if num - 1 not in numSet:
                length = 1

                while num + length in numSet:
                    length += 1
                
                curMax = max(curMax, length)

        return curMax


























        # if len(nums) == 0 or len(nums) == 1:
        #     return len(nums)

        # numsSet = set(nums)

        # curMax = 0

        # for num in nums:
        #     if (num - 1) not in numsSet:
        #         length = 1

        #         while num + length in numsSet:
        #             length += 1
                
        #         curMax = max(curMax, length)
        
        # return curMax


        