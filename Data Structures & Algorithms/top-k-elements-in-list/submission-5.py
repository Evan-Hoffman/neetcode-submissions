class Solution:
    from collections import Counter
    import heapq

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCts = Counter(nums)

        heap = []

        for num, ct in numCts.items():
            if len(heap) < k:
                heapq.heappush(heap, (ct, num))
            else:
                heapq.heappushpop(heap, (ct, num))
        
        return [num for ct, num in heap]



























        # counts = Counter(nums)

        # heap = []

        # for (num, freq) in counts.items():
        #     if len(heap) < k:
        #         heapq.heappush(heap, (freq, num))
        #     else:
        #         heapq.heappushpop(heap, (freq, num))
        
        # return [val for freq, val in heap]



        