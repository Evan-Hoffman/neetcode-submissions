# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ##perform DFS, add a curMax param
        ##each level, return 1 or 0 for self compared to max, + results of children

        def dfs(node, curMax) -> int:
            if not node:
                return 0
            
            if node.val >= curMax:
                res = 1
            else:
                res = 0
            
            res += dfs(node.left, max(curMax, node.val))
            res += dfs(node.right, max(curMax, node.val))
            return res
        
        return dfs(root, root.val)
        