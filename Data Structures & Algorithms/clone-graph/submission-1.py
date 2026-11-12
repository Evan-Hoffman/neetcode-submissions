"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node 

        oldToNew = {}

        stack = [node]

        ##Add all original nodes to map
        while stack:
            topNode = stack.pop()

            oldToNew[topNode] = Node(topNode.val)

            for neighbor in topNode.neighbors:
                if neighbor not in oldToNew:
                    stack.append(neighbor)

        ##Add neighbors:
        stack = [node]
        visited = set()

        while stack:
            topNode = stack.pop()
            visited.add(topNode)
            newNeighborsList = []

            for neighbor in topNode.neighbors:
                newNeighborsList.append(oldToNew[neighbor])
                if neighbor not in visited:
                    stack.append(neighbor)
            
            oldToNew[topNode].neighbors = newNeighborsList
                

        
        return oldToNew[node]
        