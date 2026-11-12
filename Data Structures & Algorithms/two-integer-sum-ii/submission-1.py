class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        start, end = 0, len(numbers) - 1

        while start < end:
            diff = target - numbers[start] - numbers[end]

            if diff == 0:
                return [start + 1, end + 1]
            
            elif diff > 0:
                start += 1
            
            elif diff < 0:
                end -= 1
        
        return
        