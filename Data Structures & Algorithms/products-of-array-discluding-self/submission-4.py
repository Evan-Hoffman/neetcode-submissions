class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[1, 2, 4, 6]

        #[1, 1, 1, 1]
        #[1, 1, 2, 8]
        #[48, 24, 6, 1]

        res = [1] * len(nums)

        rollingProduct = 1
        for i, num in enumerate(nums):
            res[i] *= rollingProduct
            rollingProduct *= num
        
        rollingProduct = 1
        for j in range(len(nums) - 1, -1, -1):
            res[j] *= rollingProduct
            rollingProduct *= nums[j]
        
        return res

        