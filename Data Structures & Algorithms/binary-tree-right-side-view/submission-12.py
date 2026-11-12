# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ##Recursive DFS:
        self.res = []

        def dfs(node, level):
            if not node:
                return 
            
            if level == len(self.res):
                self.res.append(node.val)
            
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        
        dfs(root, 0)
        return self.res


        ##Iterative DFS:
        # res = []

        # stack = []

        # if root:
        #     stack.append((root, 0))
        
        # while stack:
        #     node, level = stack.pop()

        #     if len(res) == level:
        #         res.append(node.val)
            
        #     if node.left:
        #         stack.append((node.left, level + 1))
        #     if node.right:
        #         stack.append((node.right, level + 1))
            
            
        # return res


        ## BFS:
        # res = []

        # q = deque()

        # if root:
        #     q.append(root)
        
        # while q:
        #     for i in range(len(q)):
        #         node = q.popleft()

        #         if i == 0:
        #             res.append(node.val)
                
        #         if node.right:
        #             q.append(node.right)
        #         if node.left:
        #             q.append(node.left)
            
        # return res

        


















        # result = []
        # if not root:
        #     return result

        # q = deque([root])

        # while q:
        #     result.append(q[-1].val)
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)

        # return result
        
        