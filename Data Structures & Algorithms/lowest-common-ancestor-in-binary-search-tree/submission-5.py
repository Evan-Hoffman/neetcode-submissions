# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ##Recursive
        # if not root or not p or not q:
        #     return None
        
        # if max(p.val, q.val) < root.val:
        #     return self.lowestCommonAncestor(root.left, p, q)
        
        # elif min(p.val, q.val) > root.val:
        #     return self.lowestCommonAncestor(root.right, p, q)
        
        # return root

        ##Iterative:

        ptr = root
        qVal = q.val
        pVal = p.val

        while ptr:
            if ptr.val > max(qVal, pVal):
                ptr = ptr.left
            
            elif ptr.val < min(qVal, pVal):
                ptr = ptr.right
            
            else:
                return ptr
        


























        # while root:
        #     if root.val < p.val and root.val < q.val:
        #         root = root.right
        #     elif root.val > p.val and root.val > q.val:
        #         root = root.left
        #     else:
        #         return root

        