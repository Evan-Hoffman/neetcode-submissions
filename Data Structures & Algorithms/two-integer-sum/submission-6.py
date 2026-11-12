class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}

        for i, num in enumerate(nums):
            twin = target - num
            if twin in numsMap:
                return [numsMap[twin], i]
            
            if num not in numsMap:
                numsMap[num] = i
                