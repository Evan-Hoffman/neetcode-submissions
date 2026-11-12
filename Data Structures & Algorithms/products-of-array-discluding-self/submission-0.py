class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ## [48, 24, 6, 1]
        ## [1, 1, 2, 8]
        ## [1, 2, 4, 6]

        leftList = [1] * len(nums)
        rightList = [1] * len(nums)

        ptr1 = 0
        ptr2 = 1

        while ptr2 < len(nums):
            leftList[ptr2] = leftList[ptr1] * nums[ptr1]
            ptr1 += 1
            ptr2 += 1
        
        ptr1 = len(nums) - 1
        ptr2 = len(nums) - 2

        while ptr2 >= 0:
            rightList[ptr2] = rightList[ptr1] * nums[ptr1]
            ptr1 -= 1
            ptr2 -= 1
        
        for i in range(len(nums)):
            leftList[i] = leftList[i] * rightList[i]

        return leftList

