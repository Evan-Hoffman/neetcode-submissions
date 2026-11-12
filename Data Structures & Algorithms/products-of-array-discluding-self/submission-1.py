class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 4, 6]
        # [1, 1, 2, 8]
        # [48, 24, 6, 1]
        
        res = [1] * len(nums)

        rollingProduct = 1

        for i in range(len(nums)):
            res[i] *= rollingProduct
            rollingProduct *= nums[i]
        
        rollingProduct = 1

        for i in range(len(nums) -1, -1, -1):
            res[i] *= rollingProduct
            rollingProduct *= nums[i]
        
        return res
        
