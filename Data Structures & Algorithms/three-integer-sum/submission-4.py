class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ## sort the input
        ## use 3 pointers, 1 starting at the left

        sortedNums = sorted(nums)

        solutions = []


        for i, val in enumerate(sortedNums):
            if i > 0 and sortedNums[i - 1] == val:
                continue
            
            ptr1, ptr2 = i + 1, len(nums) -1

            while ptr1 < ptr2:
                threeSum = val + sortedNums[ptr1] + sortedNums[ptr2]
                if threeSum > 0:
                    ptr2 -= 1
                elif threeSum < 0:
                    ptr1 += 1
                else:
                    solutions.append([val, sortedNums[ptr1], sortedNums[ptr2]])
                    ptr1 += 1
            
                    while sortedNums[ptr1] == sortedNums[ptr1 - 1] and ptr1 < ptr2:
                        ptr1 += 1
        
        return solutions
        