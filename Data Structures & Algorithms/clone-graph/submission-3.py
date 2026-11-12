"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        ##BFS:
        if not node:
            return None
        oldToNew = {node: Node(node.val)}

        q = deque()
        q.append(node)

        while q:
            curNode = q.popleft()


            for nei in curNode.neighbors:
                if nei not in oldToNew:
                    oldToNew[nei] = Node(nei.val)
                    q.append(nei)
                oldToNew[curNode].neighbors.append(oldToNew[nei])
        
        return oldToNew[node]







        ##DFS:
        # oldToNew = {}

        # def dfs(node):
        #     if node in oldToNew:
        #         return oldToNew[node]
            
        #     oldToNew[node] = Node(node.val)
        #     nei = []

        #     for neighbor in node.neighbors:
        #         newNode = dfs(neighbor)
        #         nei.append(newNode)
            
        #     oldToNew[node].neighbors = nei
        #     return oldToNew[node]
        
        
        # return dfs(node) if node else None
