# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    from collections import deque
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ##Recursive DFS:

        def dfs(node, floor, ceiling):
            if not node:
                return True
            
            if node.val <= floor or node.val >= ceiling:
                return False
            
            return dfs(node.left, floor, node.val) and dfs(node.right, node.val, ceiling)
        

        return dfs(root, float("-inf"), float("inf"))
        
