class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        stacks = [[] for i in range(len(hand) // groupSize)]

        heapq.heapify(hand)

        for j in range(len(hand)):
            minVal = heapq.heappop(hand)
            added = False

            for stack in stacks:
                if stack and len(stack) < groupSize and stack[-1] == minVal - 1:
                    stack.append(minVal)
                    added = True
                    break
                elif not stack:
                    stack.append(minVal)
                    added = True
                    break
                else:
                    continue
            
            if not added:
                return False
        
        return True
        