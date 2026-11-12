class TimeMap:

    def __init__(self):
        self.map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = [(timestamp, value)]
        else:
            self.map[key].append((timestamp, value))
       

    def get(self, key: str, timestamp: int) -> str:
        values = self.map.get(key, [])

        res = ""

        lo, hi = 0, len(values) - 1
        
        while lo <= hi:
            mid = (lo + hi) // 2

            midStamp = values[mid][0]

            if midStamp <= timestamp:
                res = values[mid][1]
                lo = mid + 1
            else:
                hi = mid - 1

        return res
        