class Solution:
    def jump(self, nums: List[int]) -> int:

        L, R = 0, 0
        ct = 0

        while R < len(nums) - 1:
            ct += 1

            newR = R
            for i in range(L, R + 1, 1):
                newR = max(newR, nums[i] + i)
            
            L = R + 1
            R = newR
        
        return ct


        