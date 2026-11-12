# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.curMax = 0

        ##recursive DFS:

        def height(node):
            if not node:
                return 0
            
            self.curMax = max(self.curMax, height(node.left) +  height(node.right))
            
            return 1 + max(height(node.left), height(node.right))
        
        height(root)
        return self.curMax

















        ##The diameter of a BT is the maximimum of the sums of the left and right maxheights of each node
        # recursive DFS
        # self.curMax = 0

        # def height( root: Optional[TreeNode] ) -> int:
        #     if not root:
        #         return 0
            
        #     leftHeight = height(root.left)
        #     rightHeight = height(root.right)

        #     self.curMax = max(self.curMax, leftHeight + rightHeight)
        #     return 1 + max(height(root.left), height(root.right))
        
        # height(root)

        # return self.curMax

 




















        

        