class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res, curSubset = [], []

        def dfs(candidates, target, i, curSum, curSubset, res):
            if curSum == target:
                res.append(curSubset.copy())
                return
                
            if i >= len(candidates) or curSum > target:
                return
            
            
            
            ##include candidate[i]
            curSubset.append(candidates[i])
            dfs(candidates, target, i + 1, curSum + candidates[i], curSubset, res)


            ##don't include any candidate[i]
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            curSubset.pop()
            dfs(candidates, target, i + 1, curSum, curSubset, res)
        
        dfs(candidates, target, 0, 0, curSubset, res)
        return res


