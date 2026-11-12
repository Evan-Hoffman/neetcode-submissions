class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for (x, y) in points:
            dist = math.sqrt(math.pow((0 - x), 2) + math.pow((0 - y), 2)) * -1

            if len(heap) < k:
                heapq.heappush(heap, (dist, [x, y]))
            else:
                heapq.heappushpop(heap, (dist, [x, y]))
        
        return [pt for dist, pt in heap]

        