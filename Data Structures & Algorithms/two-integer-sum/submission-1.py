class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}

        for index, num in enumerate(nums):
            difference = target - num
            if difference in pairs:
                return [pairs[difference], index]
            else:
                pairs[num] = index
    
