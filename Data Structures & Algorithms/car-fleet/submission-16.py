class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        ##  [3, 4, 5, 6, 7, 8]
        ##  [4, 4, 4, 4, 4, 4]
        ## zip, sort by position ASC

        ## iterate left to right
        ## calculate ETA
        ## iff stack empty or top of stack > ETA, push
        ## else pop push
        ## return len(stack)

        zipped = list(zip(position, speed))
        zipped.sort()

        fleets = []

        for i in range(len(zipped)):
            eta = (target - zipped[i][0]) / zipped[i][1]

            # if not fleets or fleets[-1] > eta:
            #     fleets.append(eta)
            #     continue
            
            while fleets and fleets[-1] <= eta:
                fleets.pop()

            fleets.append(eta)

        
        return len(fleets)
        