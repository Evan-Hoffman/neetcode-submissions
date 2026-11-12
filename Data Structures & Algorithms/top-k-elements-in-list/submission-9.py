class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)

        pairs = [(count, num) for num, count in freqs.items()]

        sorted_pairs = sorted(pairs)
        res = []

        for i in range(len(sorted_pairs) -1, len(sorted_pairs) - k - 1,  -1):
            res.append(sorted_pairs[i][1])
        
        return res


        