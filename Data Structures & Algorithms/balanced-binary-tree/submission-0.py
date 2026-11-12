# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.isBal = True

        def height(curr):
            if not curr:
                return 0
            
            leftHeight = height(curr.left)
            rightHeight = height(curr.right)

            if abs(leftHeight - rightHeight) > 1:
                self.isBal = False

            return 1 + max(leftHeight, rightHeight)
        
        height(root)
        return self.isBal
        