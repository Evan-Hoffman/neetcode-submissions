class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ##BFS:
        adjList = {i: [] for i in range(n)}

        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        
        visited = set()

        q = collections.deque([(0, None)])

        while q:
            node, parent = q.popleft()
            if node in visited:
                return False
            
            visited.add(node)

            for child in adjList[node]:
                if child != parent:
                    q.append((child, node))
            
        return len(visited) == n
                    







        ##DFS:
        # adjList = {i: [] for i in range(n)}

        # for n1, n2 in edges:
        #     adjList[n1].append(n2)
        #     adjList[n2].append(n1)
        
        # visited = set()

        # def dfs(node, parent):
        #     if node in visited:
        #         return False
            
        #     visited.add(node)
        #     for child in adjList[node]:
        #         if child != parent:
        #             if not dfs(child, node):
        #                 return False
            
        #     return True
        
        # return dfs(0, None) and len(visited) == n



        