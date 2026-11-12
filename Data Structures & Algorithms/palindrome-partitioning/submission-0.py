class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, partitions = [], []

        def dfs(s, partitions, i):
            if i >= len(s):
                res.append(partitions.copy())
                return

            for j in range(i, len(s)):
                base = s[i]
                l, r = i, j
                isPal = True
                while l < r:
                    if s[l] != s[r]:
                        isPal = False
                        break
                    
                    l += 1
                    r -= 1
                
                if isPal:
                    partitions.append(s[i: j + 1])
                    dfs(s, partitions, j + 1)
                    partitions.pop()
            
            
        dfs(s, partitions, 0)
        return res

        