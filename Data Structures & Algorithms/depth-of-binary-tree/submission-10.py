# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ##BFS
        depth = 0


        if not root:
            return depth

        q = deque()
        q.append(root)

        while q:
            depth += 1
            for i in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return depth



























        ## BFS:

        # level = 0

        # if not root:
        #     return level

        # queue = deque()
        # queue.append(root)

        # while queue:

        #     for i in range(len(queue)):
        #         node = queue.popleft()

        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
                
        #     level += 1

        # return level

        ##recursive DFS:
        # if not root:
        #     return 0
        
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        ##iterative DFS:
        # if not root:
        #     return 0

        # stack = [(root, 1)]
        # curMax = 0

        # while stack:
        #     node, depth = stack.pop()
        #     curMax = max(curMax, depth)

        #     if node.left:
        #         stack.append((node.left, depth + 1))
        #     if node.right:
        #         stack.append((node.right, depth + 1))

        # return curMax 
























        #DFS
        # if not root:
        #     return 0
        
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        ##BFS
        # queue = deque()

        # level = 0

        # if root:
        #     queue.append(root)

        # while len(queue) > 0:
        #     level += 1

        #     for i in range(len(queue)):
        #         node = queue.popleft()


        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        
        # return level

    
        
        