class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        l, r = 0, len(nums) - 1
        k = 0

        while l < r:
            if nums[l] != val:
                l += 1
            elif nums[r] == val:
                r -= 1
            else:
                nums[l] = nums[r]
                nums[r] = val
                l += 1
                r -= 1
                k += 1
        
        return l + 1 if nums[l] != val else l
            
        

        