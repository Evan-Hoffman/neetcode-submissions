class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)

        buckets = [[] for i in range(len(nums))]

        for num, count in freqs.items():
            buckets[count - 1].append(num)
        
        res = []

        while buckets and len(res) < k:
            vals = buckets.pop()

            while vals and len(res) < k:
                res.append(vals.pop())
        
        return res



        # freqs = Counter(nums)

        # pairs = [(count, num) for num, count in freqs.items()]

        # pairs.sort()
        # res = []

        # while len(res) < k:
        #     res.append(pairs.pop()[1])
        
        # return res


        