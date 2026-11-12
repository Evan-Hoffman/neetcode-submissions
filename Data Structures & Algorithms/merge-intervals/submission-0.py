class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervalsSorted = sorted(intervals)

        res = []
        last = []

        for i in range(len(intervalsSorted)):
            cur = intervalsSorted[i]
            if not len(last):
                last = cur
            
            else:
                if last[1] >= cur[0]:
                    last = [min(last[0], cur[0]), max(last[1], cur[1])]
                else:
                    res.append(last)
                    last = cur
        
        if last:
            res.append(last)

        return res
        