class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= target:
                target = i
            # else:
            #     dist += 1
        
        return target == 0
        