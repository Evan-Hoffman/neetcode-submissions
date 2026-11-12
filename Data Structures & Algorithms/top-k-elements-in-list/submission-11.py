class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)

        pairs = [(count, num) for num, count in freqs.items()]

        pairs.sort()
        res = []

        while len(res) < k:
            res.append(pairs.pop()[1])
        
        return res


        