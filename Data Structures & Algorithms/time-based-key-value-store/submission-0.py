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
            list = self.map[key]

            if timestamp < list[0][0]:
                return ""
            
            if timestamp > list[-1][0]:
                return list[-1][1]

            l, r = 0, len(list) - 1
            mid = 0

            while l < r:
                mid = (l + r) // 2

                if list[mid][0] > timestamp:
                    r = mid
                elif list[mid][0] < timestamp:
                    l = mid + 1
                else:
                    return list[mid][1]
            
            if list[l][0] > timestamp:
                return list[l-1][1]

            return list[l][1]    

        else:
            return ""
