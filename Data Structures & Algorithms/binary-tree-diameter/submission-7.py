# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #diameter = height of left + height of right
        self.curMax = 0
        
        def height(node) -> int:
            if not node:
                return 0
            
            lHeight = height(node.left)
            rHeight = height(node.right)
            self.curMax = max(self.curMax, lHeight + rHeight)

            return 1 + max(lHeight, rHeight)
        
        height(root)
        return self.curMax
    
        
        

      