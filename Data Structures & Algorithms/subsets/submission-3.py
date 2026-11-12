class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[nums[0]]]

        for i in range(1, len(nums)):
            for j in range(len(res)):
                cop = res[j].copy()
                cop.append(nums[i])
                res.append(cop)
            res.append([nums[i]])

        res.append([])
        return res

        