class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, num in enumerate(nums):
            if num > 0:
                break
            
            if i > 0 and nums[i - 1] == num:
                continue
            
            l, r = i + 1, len(nums) - 1
            target = 0 - num

            while l < r:
                cur = nums[l] + nums[r]

                if cur == target:
                    res.append([num, nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                elif cur > target:
                    r -= 1
                else:
                    l += 1
        
        return res



        