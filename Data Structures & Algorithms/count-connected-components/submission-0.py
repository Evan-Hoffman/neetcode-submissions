class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        visited = set()

        nodeToEdges = {i: [] for i in range(n)}

        for n1, n2 in edges:
            nodeToEdges[n1].append(n2)
            nodeToEdges[n2].append(n1)

        def dfs(node, last):
            if node in visited:
                return
            
            visited.add(node)

            for neighbor in nodeToEdges[node]:
                if neighbor != last:
                    dfs(neighbor, node)
            
        for i in range(n):
            if i in visited:
                continue
            else:
                res += 1
                dfs(i, -1)
        
        return res

