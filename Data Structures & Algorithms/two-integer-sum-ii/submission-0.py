class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ptr1, ptr2 = 0, len(numbers) - 1

        while numbers[ptr1] + numbers[ptr2] != target:
            sum = numbers[ptr1] + numbers[ptr2]
            if sum > target:
                ptr2 -= 1
            elif sum < target:
                ptr1 += 1
        
        return [ptr1 + 1, ptr2 + 1]

        