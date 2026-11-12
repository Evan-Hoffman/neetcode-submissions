class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort()

        ct = 1
        timeToBeat = (target - cars[-1][0]) / cars[-1][1]

        for i in range(len(cars) - 2, -1, -1):
            p, s = cars[i]
            timeToDest = (target - p) / s

            if timeToDest > timeToBeat:
                ct += 1
                timeToBeat = timeToDest
        
        return ct
        