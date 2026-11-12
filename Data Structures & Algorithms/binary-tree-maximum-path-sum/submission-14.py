# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.curMax = float("-inf")

        def dfs(node):
            if not node:
                return 0
            
            maxLeft = max(dfs(node.left), 0)
            maxRight = max(dfs(node.right), 0)
            self.curMax = max(self.curMax, node.val + maxLeft + maxRight)

            return node.val + max(maxLeft, maxRight)
        
        dfs(root)
        return self.curMax
        




















        # self.curMax = root.val
        
        # def dfs(curr):
        #     if not curr:
        #         return 0
            
        #     sumLeft = dfs(curr.left)
        #     sumRight = dfs(curr.right)
        #     leftMax = max(sumLeft, 0)
        #     rightMax = max(sumRight, 0)
        #     self.curMax = max(self.curMax, leftMax + rightMax + curr.val)
           
        #     return max(curr.val + leftMax, curr.val + rightMax)
        
        # dfs(root)
        # return self.curMax

        