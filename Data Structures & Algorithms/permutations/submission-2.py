class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, curPerm = [], []
        options = nums.copy()

        def dfs(options, curPerm, nums, res):
            if len(curPerm) == len(nums):
                res.append(curPerm.copy())
                return
            

            for i in range(len(options)):
                curPerm.append(options[i])
                dfs(options[0: i] + options[i + 1:], curPerm, nums, res)
                curPerm.pop()
        
        dfs(options, curPerm, nums, res)
        return res
            


        