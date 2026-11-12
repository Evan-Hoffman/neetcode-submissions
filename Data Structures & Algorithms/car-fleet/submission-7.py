class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
       ##sort the position array (keeping speeds tied to)
       ## going furtherest car to closest car (reverse):
        ##calculate t, time to destination. 
        ##check top of stack; if top has a greater time to destination, this car will become part of that fleet, so discard
        ##else, add it to the stack
    
       ## return the length of the stack

        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)

        stack = []

        for p, s in cars:
            t = (target - p) / s

            if not stack:
                stack.append(t)
            
            else:
                if not t <= stack[-1]:
                    stack.append(t)
        
        return len(stack)
    
        # pairs = [(p, s) for p, s in zip(position, speed)]

        # pairs.sort(reverse=True)
        # stack = []

        # for p, s in pairs:
        #     stack.append((target - p) / s)
        #     if len(stack) >= 2  and stack[-1] <= stack[-2]:
        #         stack.pop()
        
        # return len(stack)


        