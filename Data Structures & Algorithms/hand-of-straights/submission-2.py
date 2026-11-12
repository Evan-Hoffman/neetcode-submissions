class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        counts = Counter(hand)

        minH = [val for val in counts.keys()]
        heapq.heapify(minH)

        
        #{1: 1, 2: 2, 3: 2, 4: 2, 5: 1}
        #heap = [1, 2, 3, 4, 5]
        while minH:
            smallest = heapq.heappop(minH)

            if smallest in counts:
                need = counts[smallest]
            
                for i in range(groupSize):
                    toFind = smallest + i
                    if toFind not in counts or counts[toFind] < need:
                        return False
                    elif counts[toFind] == need:
                        counts.pop(toFind)
                    else:
                        counts[toFind] -= need
        
        return False if counts else True
        