class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ## observe the array exists only as either 2 sorted arrays or 1 sorted array
        ## while it is 2 sorted arrays, use binary search to determine which array we are in
        ##if mid is in left-array, check if target is between min(left) and mid. 
        ## If yes, we set right to mid. If not, we set left to mid+1
        ## if mid is in right-array, check if target is between min(mid) and right.
        ## if yes, we set left to mid + 1. If not, we set right to mid - 1
        
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if nums[mid] == target:
                return mid

            ##we are in left array if nums[mid] > nums[hi]
            elif nums[mid] >= nums[hi]:
                if target >= nums[lo] and target <= nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            
            ##we are in the right array
            else:
                if nums[mid] < target and nums[hi] >= target:
                    lo = mid + 1
                else:
                    hi = mid - 1
        
        return -1
            
            























        # left, right = 0, len(nums) - 1
        
        # while left <= right:
        #     mid = (left + right) // 2

        #     if nums[mid] == target:
        #         return mid
            
        #     ## we are in left increasing array
        #     elif nums[mid] >= nums[left]:
        #         if target >= nums[left] and target < nums[mid]:
        #             right = mid - 1
        #         else:
        #             left = mid + 1
            
        #     ##we are in right increasing array
        #     else:
        #         if target > nums[mid] and target <= nums[right]:
        #             left = mid + 1
        #         else:
        #             right = mid - 1
        
        # return -1

