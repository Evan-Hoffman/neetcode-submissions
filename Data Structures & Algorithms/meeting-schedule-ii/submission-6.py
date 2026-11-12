"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = [t.start for t in intervals]
        ends = [t.end for t in intervals]

        starts.sort()
        ends.sort()

        s = 0
        active = 0
        curMax = 0

        for e in range(len(ends)):
            endTime = ends[e]

            while s < len(starts) and starts[s] < endTime:
                active += 1
                s += 1
            
            curMax = max(curMax, active)
            active -= 1
        
        return curMax



        