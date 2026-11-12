class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result, curSubset = [], []

        def helper(i, curSubset):
            if i >= len(nums):
                result.append(curSubset.copy())
                return
            
            ## choose to include element at i:
            curSubset.append(nums[i])
            helper(i + 1, curSubset)

            ## choose not to include element at i:
            curSubset.pop()
            helper(i + 1, curSubset)
        
        helper(0, curSubset)
        return result
        