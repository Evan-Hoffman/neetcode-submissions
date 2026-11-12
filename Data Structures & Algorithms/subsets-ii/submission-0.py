class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res, curSubset = [], []
        self.helper(0, curSubset, res, nums)
        return res
    
    def helper(self, i, curSubset, res, nums):
        if i >= len(nums):
            res.append(curSubset.copy())
            return
        
        ##include nums[i]
        curSubset.append(nums[i])
        self.helper(i + 1, curSubset, res, nums)


        ##dont include nums[i] or any of its copies
        i += 1
        while i < len(nums) and nums[i - 1] == nums[i]:
            i += 1
        
        curSubset.pop()
        self.helper(i, curSubset, res, nums)
        