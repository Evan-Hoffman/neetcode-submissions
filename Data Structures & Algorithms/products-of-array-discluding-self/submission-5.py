class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ## [1, 1, 2, 8]
        ## [1, 2, 4, 6]
        # 1 x 6 x 2
        # 6 x 4 = 24
        # 24 x 1 = 24
        #

        res = [1] * len(nums)

        product = 1
        for i in range(1, len(nums)):
            product = product * nums[i-1]
            res[i] = product
        
        product = 1
        for i in range(len(nums) -2, -1, -1):
            product = product * nums[i + 1]
            res[i] = res[i] * product
        
        return res
        