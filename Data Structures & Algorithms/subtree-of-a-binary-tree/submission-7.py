# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
            if not t1 and not t2:
                return True
            
            if not t1 or not t2 or t1.val != t2.val:
                return False
            
            return isSameTree(t1.left, t2.left) and isSameTree(t1.right, t2.right)
        
        if not root:
            return False
        
        if root.val == subRoot.val and isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

















        
        # def isSameTree(treeA, treeB) -> bool:
        #     if not treeA and not treeB:
        #         return True
            
        #     if (treeA and treeB) and (treeA.val == treeB.val):
        #         return isSameTree(treeA.left, treeB.left) and isSameTree(treeA.right, treeB.right)
        #     else:
        #         return False
        
        # if not root:
        #     return False
        
        # if root.val == subRoot.val:
        #     if isSameTree(root, subRoot):
        #         return True
        
        # return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
                