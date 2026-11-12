class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)

        buckets = [[] for i in range(len(nums))]

        for num, count in freqs.items():
            buckets[count - 1].append(num)
        
        res = []

        for i in range(len(buckets) - 1,-1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        return res



        # freqs = Counter(nums)

        # pairs = [(count, num) for num, count in freqs.items()]

        # pairs.sort()
        # res = []

        # while len(res) < k:
        #     res.append(pairs.pop()[1])
        
        # return res


        