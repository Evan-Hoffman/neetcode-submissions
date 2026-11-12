class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sortedInts = sorted(intervals)

        ct = 0
        prevEnd = sortedInts[0][1]

        for i in range(1, len(sortedInts)):
            cur = sortedInts[i]

            if cur[0] < prevEnd:
                prevEnd = min(cur[1], prevEnd)
                ct += 1
            
            else:
                prevEnd = cur[1]
        
        return ct
