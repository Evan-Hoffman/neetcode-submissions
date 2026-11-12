# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ##Recursive DFS:
        res = []

        def dfs(node, depth):
            if not node:
                return

            if len(res) == depth:
                res.append([node.val])
            
            else:
                res[depth].append(node.val)
            
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return res





        ##BFS
        # res = []
        # if not root:
        #     return res
        
        # q = deque([root])

        # while q:
        #     level = []
        #     for i in range(len(q)):
        #         node = q.popleft()

        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
                
        #         level.append(node.val)
            
        #     res.append(level)
        
        # return res

        