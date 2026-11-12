# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    from collections import deque
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #BFS
        if not root:
            return True
        
        q = deque([(root, float("-inf"), float("inf"))])

        while q:

            for i in range(len(q)):
                node, floor, ceil = q.popleft()

                if node.val <= floor or node.val >= ceil:
                    return False
                
                if node.right:
                    q.append((node.right, node.val, ceil))
                if node.left:
                    q.append((node.left, floor, node.val))
                
        
        return True


        




        #DFS
        # def dfs(node, left, right) -> bool:
        #     if not node:
        #         return True
            
        #     if (node.val >= right or node.val <= left):
        #         return False
            
        #     return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)
        
        # return dfs(root, float("-inf"), float("inf"))




















        # def isValid(node, left, right) -> bool:
        #     if not node:
        #         return True
            
        #     if not (node.val > left and node.val < right):
        #         return False
            
        #     return isValid(node.left, left, node.val) and isValid(node.right, node.val, right)
        
        # return isValid(root, float("-inf"), float("inf"))
        

        