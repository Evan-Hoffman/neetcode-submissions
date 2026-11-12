class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ##BFS:






        ##DFS:
        res = 0
        visited = set()

        nodeToEdges = {i: [] for i in range(n)}

        for n1, n2 in edges:
            nodeToEdges[n1].append(n2)
            nodeToEdges[n2].append(n1)

        def dfs(node):
            for neighbor in nodeToEdges[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
            
        for i in range(n):
            if i in visited:
                continue
            else:
                visited.add(n)
                res += 1
                dfs(i)
        
        return res

