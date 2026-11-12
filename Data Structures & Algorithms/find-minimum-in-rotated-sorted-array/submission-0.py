class Solution:
    def findMin(self, nums: List[int]) -> int:
        ## track a min
        ## with pointers at the start and end of nums, conduct a binary search
        ## while val[start] > val[end]
        ## get mid value, decide if mid value is in left sorted poriton or right sorted poriton
        ## if in left sorted portion, search right
        ## if in right sorted poriton, search left
        ## once while loop breaks, check if left is less than min

        result = nums[len(nums) // 2]

        left, right = 0, len(nums) - 1

        while nums[left] > nums[right]:
            mid = (left + right) // 2
            midVal = nums[mid]
            result = min(result, midVal)

            if midVal >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        
        return min(result, nums[left])


        