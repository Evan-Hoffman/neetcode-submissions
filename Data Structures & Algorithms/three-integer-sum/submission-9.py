class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #[-4, -1, -1, 0, 1, 2]
        sortedNums = sorted(nums)
        triplets = []

        for i in range(len(nums)):
            if i != 0 and sortedNums[i - 1] == sortedNums[i]:
                continue

            target = 0 - sortedNums[i]

            start, end = i + 1, len(nums) - 1

            while start < end:
                tot = sortedNums[start] + sortedNums[end]

                if tot == target:
                    triplets.append([sortedNums[i], sortedNums[start], sortedNums[end]])
                    start += 1
                    end -= 1
                    while start < end and sortedNums[end + 1] == sortedNums[end]:
                        end -= 1

                elif tot > target:
                    end -= 1
                else:
                    start += 1
            
        return triplets

                
                







































        # inOrder = sorted(nums)
        # triplets = []

        # for i in range (len(inOrder)):
        #     if i != 0 and inOrder[i - 1] == inOrder[i]:
        #         continue

        #     target = 0 - inOrder[i]
        #     start, end = i + 1, len(inOrder) - 1

        #     while start < end:
        #         total = inOrder[start] + inOrder[end]

        #         if total == target:
        #             triplets.append([inOrder[i], inOrder[start], inOrder[end]])
        #             start += 1
        #             end -= 1
        #             while start < end and inOrder[end + 1] == inOrder[end]:
        #                 end -= 1
        #         elif total < target:
        #             start += 1
        #         elif total > target:
        #             end -= 1
        
        # return triplets


        