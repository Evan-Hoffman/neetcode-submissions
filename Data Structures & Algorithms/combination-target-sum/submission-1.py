class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, curSubset = [], []

        self.helper(nums, target, 0, 0, curSubset, res)
        return res
    

    def helper(self, nums, target, i, curSum, curSubset, res):
        if curSum > target or i >= len(nums):
            return
        
        if curSum == target:
            res.append(curSubset.copy())
            return
        
        curSubset.append(nums[i])
        
        ##include nums[i]
        self.helper(nums, target, i, curSum + nums[i], curSubset, res)

        ##don't include nums[i]
        curSubset.pop()
        self.helper(nums, target, i + 1, curSum, curSubset, res)
        