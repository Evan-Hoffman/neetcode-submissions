class Solution:
    def findDuplicate(self, nums: List[int]) -> int:







































        slow, fast = 0, 0

        while True:
            slow = nums[slow] #1 3 2 4
            fast = nums[nums[fast]] #3 4 4 4

            if slow == fast:
                break
        
        slow2 = 0

        while slow2 != slow:
            slow = nums[slow] # 2 4 2
            slow2 = nums[slow2] # 1 3 2

        
        return slow
        


        