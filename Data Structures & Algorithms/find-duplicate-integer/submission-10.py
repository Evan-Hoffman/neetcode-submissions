class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # [1,2,3,2,2]
        #  0 1 2 3 4
        #f: 0, 2, 2
        #s: 0, 1, 2

        # [1, 3, 4, 4, 4]
        #f: 0, 2, 4, 4
        #s: 0, 1, 2, 4

        #[1, 3, 4, 2, 2]
        #f: 0, 3, 4, 4,
        #s: 0, 1, 3, 4, 2, 4, 2, 4
        #s2:            1, 3, 4, 2

        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow2 = 0
        while slow2 != slow:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow







































        # slow, fast = 0, 0

        # while True:
        #     slow = nums[slow] #1 3 2 4
        #     fast = nums[nums[fast]] #3 4 4 4

        #     if slow == fast:
        #         break
        
        # slow2 = 0

        # while slow2 != slow:
        #     slow = nums[slow] # 2 4 2
        #     slow2 = nums[slow2] # 1 3 2

        
        # return slow
        


        