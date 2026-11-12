# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    from collections import deque
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ##BFS
        if not root:
            return 0

        q = deque()

        q.append((root, 1))

        curMax = 0

        while q:
            node, depth = q.popleft()
            curMax = max(curMax, depth)

            if node.left:
                q.append((node.left, depth + 1))
            
            if node.right:
                q.append((node.right, depth + 1))
        
        return curMax




        ##Recursive DFS:
        # if not root:
        #     return 0
        
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        