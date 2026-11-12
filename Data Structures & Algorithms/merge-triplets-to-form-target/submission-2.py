class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            for index, val in enumerate(t):
                if val == target[index] and index not in found:
                    found.add(index)

        return len(found) == 3

            
            


        