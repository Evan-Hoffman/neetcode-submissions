class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        heap = []
        ptr = 0
        res = {}

        for q in sorted(queries):
            while ptr < len(intervals) and intervals[ptr][0] <= q:
                l, r = intervals[ptr]
                heapq.heappush(heap, (r - l + 1, r))
                ptr += 1
            
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            res[q] = heap[0][0] if heap else -1
        
        return [res[q] for q in queries]
            

            



        