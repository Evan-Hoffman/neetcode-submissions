# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ##The diameter of a BT is the maximimum of the sums of the left and right maxheights of each node
        self.curMax = 0

        def height(curr):
            if not curr:
                return 0
            
            leftHeight = height(curr.left)
            rightHeight = height(curr.right)
            
            self.curMax = max(self.curMax, leftHeight + rightHeight)
            return 1 + max(leftHeight, rightHeight)
        
        height(root)

        return self.curMax

        

        