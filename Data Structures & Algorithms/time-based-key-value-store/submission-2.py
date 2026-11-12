class TimeMap:

    def __init__(self):
        self.map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = [(timestamp, value)]
        else:
            self.map[key].append((timestamp, value))
       

    def get(self, key: str, timestamp: int) -> str:
        if key in self.map:
            values = self.map[key]

            lo, hi = 0, len(values) - 1
            #[2 5 7 9] 3
            #l: 0, 0
            #h: 3, 0

            #[2 5 7 9] 8
            #l: 0, 1, 2, 3
            #h: 3, 3, 3, 3

            #[2 5 7 9] 1
            #l: 0, 0
            #h: 3, 0

            
            while lo <= hi and hi >= 0:
                mid = (lo + hi) // 2

                midStamp = values[mid][0]

                if midStamp < timestamp:
                    lo = mid + 1
                
                elif midStamp > timestamp:
                    hi = mid - 1
                
                else:
                    return values[mid][1]
            
            return values[hi][1] if hi >= 0 else ""
        

        return ""
        