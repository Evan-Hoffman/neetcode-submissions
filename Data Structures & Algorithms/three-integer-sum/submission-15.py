class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = 0 - nums[i]

            L, R = i + 1, len(nums) - 1

            while L < R:
                if nums[L] + nums[R] > target:
                    R -= 1
                elif nums[L] + nums[R] < target:
                    L += 1
                else:
                    res.append([nums[i], nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
                    # while L < R and nums[R] == nums[R + 1]:
                    #     R -= 1
            
        return res
                
        