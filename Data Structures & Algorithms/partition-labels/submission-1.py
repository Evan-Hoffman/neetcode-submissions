class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # {
        #     x: 3
        #     y: 4
        #     z: 7
        #     b: 9
        #     i: 10
        #     s: 11
        #     l: 12
        # }

        lastIndex = {}

        for i, c in enumerate(s):
            lastIndex[c] = i
        
        res = []
        size = end = 0

        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])

            if end == i:
                res.append(size)
                size = 0
        
        return res





    

        