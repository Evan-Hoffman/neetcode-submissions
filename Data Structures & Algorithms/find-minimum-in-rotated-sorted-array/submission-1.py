class Solution:
    def findMin(self, nums: List[int]) -> int:
        ##given there are 2 sorted arrays, we expect the min at the beggining of the right array
        ## we want to binary search, updating our start and end until we are looking at purely the right array
        start, end = 0, len(nums) - 1
        
        while nums[start] > nums[end]:
            mid = (start + end) // 2

            if nums[mid] > nums[end]:
                start = mid + 1
            elif nums[mid] < nums[end]:
                end = mid
        
        return nums[start]


























        ## track a min
        ## with pointers at the start and end of nums, conduct a binary search
        ## while val[start] > val[end]
        ## get mid value, decide if mid value is in left sorted poriton or right sorted poriton
        ## if in left sorted portion, search right
        ## if in right sorted poriton, search left
        ## once while loop breaks, check if left is less than min

        # result = nums[len(nums) // 2]

        # left, right = 0, len(nums) - 1

        # while nums[left] > nums[right]:
        #     mid = (left + right) // 2
        #     midVal = nums[mid]
        #     result = min(result, midVal)

        #     if midVal >= nums[left]:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        
        # return min(result, nums[left])


        