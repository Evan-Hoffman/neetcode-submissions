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


        