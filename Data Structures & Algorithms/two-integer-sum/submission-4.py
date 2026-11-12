class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIndices = {}

        for index, num in enumerate(nums):
            dif = target - num
            if dif in numIndices:
                return [numIndices[dif], index]
            
            numIndices[num] = index
        
