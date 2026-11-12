class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combos = []
        self.helper(0, nums, [], 0, target, combos)
        return combos

    def helper(self, i, nums, curCom, curSum, target, combos):
        if curSum == target:
            combos.append(curCom.copy())
            return
        
        if curSum > target or i >= len(nums):
            return
        
        #include self and repeat
        curCom.append(nums[i])
        self.helper(i, nums, curCom, curSum + nums[i], target, combos)

        ##don't include self
        curCom.pop()
        self.helper(i + 1, nums, curCom, curSum, target, combos) 


        