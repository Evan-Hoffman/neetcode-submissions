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
        L, R = 0, 0
        curEnd = lastIndex[s[L]]

        runningSet = set(s[R])
        #len(s) = 13
        #L: 5
        #R: 5
        #set: ()
        #curEnd = 7
        #res: [5, ]

        while R < len(s):
            if R == curEnd:
                res.append(R - L + 1)
                L = R + 1
                runningSet = set()
                curEnd = lastIndex[s[L]] if L < len(s) else 0

            elif s[R] not in runningSet:
                curEnd = max(curEnd, lastIndex[s[R]])
                runningSet.add(s[R])

            R += 1
        
        return res





    

        