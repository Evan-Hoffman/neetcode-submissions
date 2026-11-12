class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        inOrder = sorted(nums)
        triplets = []

        for i in range (len(inOrder)):
            if i != 0 and inOrder[i - 1] == inOrder[i]:
                continue

            target = 0 - inOrder[i]
            start, end = i + 1, len(inOrder) - 1

            while start < end:
                total = inOrder[start] + inOrder[end]

                if total == target:
                    triplets.append([inOrder[i], inOrder[start], inOrder[end]])
                    start += 1
                    end -= 1
                    while start < end and inOrder[end + 1] == inOrder[end]:
                        end -= 1
                elif total < target:
                    start += 1
                elif total > target:
                    end -= 1
        
        return triplets


        