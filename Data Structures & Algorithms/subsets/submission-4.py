class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # res = [[nums[0]]]

        # for i in range(1, len(nums)):
        #     for j in range(len(res)):
        #         cop = res[j].copy()
        #         cop.append(nums[i])
        #         res.append(cop)
        #     res.append([nums[i]])

        # res.append([])
        # return res
        res, curSet = [], []
        self.helper(nums, 0, res, curSet)
        return res
    
    def helper(self, nums, i, res, curSet):
        if i >= len(nums):
            res.append(curSet.copy())
            return
        
        ##include nums[i]
        curSet.append(nums[i])
        self.helper(nums, i + 1, res, curSet)

        curSet.pop()
        self.helper(nums, i + 1, res, curSet)
        
        
        


        