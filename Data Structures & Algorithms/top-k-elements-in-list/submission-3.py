import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}

        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1
        
        minheap = []

        for num, freq in freqs.items():
            if len(minheap) < k:
                heapq.heappush(minheap, (freq, num))
            else:
                heapq.heappushpop(minheap, (freq, num))
        
        return [h[1] for h in minheap]































        # counts = {}

        # for num in nums:
        #     counts[num] = counts.get(num, 0) + 1
        
        # heap = []

        # for (key, val) in counts.items():
        #     if (len(heap) < k):
        #         heapq.heappush(heap, (val, key))
        #     else:
        #         heapq.heappushpop(heap, (val, key))
        
        # return [key for (val, key) in heap] 