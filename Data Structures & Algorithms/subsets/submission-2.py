class Solution:
    nums = []
    result = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.result = []
        curSubset = []
        self.helper(0, curSubset)
        return self.result

    def helper(self, i, curSubset):
        if i >= len(self.nums):
            self.result.append(curSubset.copy())
            return
        
        ## choose to include element at i:
        curSubset.append(self.nums[i])
        self.helper(i + 1, curSubset)

        ## choose not to include element at i:
        curSubset.pop()
        self.helper(i + 1, curSubset)
        
        
        