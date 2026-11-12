class MedianFinder:

    def __init__(self):
        self.smallHeap = [] ## maxHeap, pops off largest, stores smallest
        self.largeHeap = [] ## minHeap, pops off minimum, stores largest 
        

    def addNum(self, num: int) -> None:
        if not self.smallHeap and not self.largeHeap:
            heapq.heappush(self.largeHeap, num)

        elif not self.smallHeap and len(self.largeHeap) == 1:
            if num < self.largeHeap[0]:
                heapq.heappush(self.smallHeap, num * -1)
            else:
                heapq.heappush(self.largeHeap, num)
                heapq.heappush(self.smallHeap, heapq.heappop(self.largeHeap) * -1)
        
        else:
            if num < self.largeHeap[0]:
                heapq.heappush(self.smallHeap, num * -1)
            else:
                heapq.heappush(self.largeHeap, num)
            
            ##heap re-balance:
            sizeSmall = len(self.smallHeap)
            sizeLarge = len(self.largeHeap)

            if abs(sizeLarge - sizeSmall) > 1:
                if sizeLarge > sizeSmall:
                    mid = heapq.heappop(self.largeHeap)
                    heapq.heappush(self.smallHeap, mid * -1)
                else:
                    mid = heapq.heappop(self.smallHeap) * -1
                    heapq.heappush(self.largeHeap, mid)

    def findMedian(self) -> float:        
        sizeSmall = len(self.smallHeap)
        sizeLarge = len(self.largeHeap)

        if sizeSmall > sizeLarge:
            return self.smallHeap[0] * -1
        elif sizeLarge > sizeSmall:
            return self.largeHeap[0]
        else:
            num1, num2 = self.smallHeap[0] * -1, self.largeHeap[0]
            return (num1 + num2) / 2.0


        
        