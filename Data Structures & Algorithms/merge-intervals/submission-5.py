class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervalsSorted = sorted(intervals)

        res = [intervalsSorted[0]]

        for i in range(len(intervalsSorted)):
            cur = intervalsSorted[i]
            lastEnd = res[-1][1]
            if lastEnd >= cur[0]:
                res[-1][1] = max(lastEnd, cur[1])
            else:
                res.append(cur)

        return res
        