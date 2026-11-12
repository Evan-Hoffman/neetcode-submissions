class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            
            else:
                return mid
        
        return -1



































        # l, r = 0, len(nums) - 1

        # while l <= r:
        #     mid = (l + r) // 2
        #     num = nums[mid]

        #     if num < target:
        #         l = mid + 1
        #     elif num > target:
        #         r = mid - 1
        #     else:
        #         return mid
        
        # return -1
        