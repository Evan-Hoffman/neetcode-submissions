class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 0
        curMax = None

        for i in range(len(nums)):
            if not counter or nums[i] == curMax:
                curMax = nums[i]
                counter += 1
            else:
                counter -= 1
                # if counter < 1:
                #     curMax = nums[i]
        return curMax
                

        