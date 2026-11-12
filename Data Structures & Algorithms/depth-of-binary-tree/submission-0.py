# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

    
        def dfs(self, root: Optional[TreeNode], depth) -> int:
            if not root:
                return depth
            
            leftDepth = dfs(self, root.left, depth + 1)
            rightDepth = dfs(self, root.right, depth + 1)

            return max(leftDepth, rightDepth)
        
        return dfs(self, root, 0)
        