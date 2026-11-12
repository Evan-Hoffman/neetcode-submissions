class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def dfs(i, curCom, curTotal):
            if curTotal == target:
                result.append(curCom.copy())
                return
            
            if curTotal > target or i >= len(candidates):
                return
            
            ##include cur num:
            curCom.append(candidates[i])
            dfs(i + 1, curCom, curTotal + candidates[i])

            ##don't include cur num:
            curCom.pop()
            while i < len(candidates) -1 and candidates[i] == candidates[i+1]:
                i += 1

            dfs(i + 1, curCom, curTotal)
        
        dfs(0, [], 0)
        return result