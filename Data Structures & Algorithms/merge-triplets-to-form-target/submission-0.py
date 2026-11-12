class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        usefulTriplets = []

        for triplet in triplets:
            toAdd = True
            for i in range(len(target)):
                if triplet[i] > target[i]:
                    toAdd = False
                    break
            
            if toAdd:
                usefulTriplets.append(triplet)
        
        for index, target in enumerate(target):
            found = False
            for triplet in usefulTriplets:
                if triplet[index] == target:
                    found = True
                    break
            
            if not found:
                return False
        
        return True

            
            


        