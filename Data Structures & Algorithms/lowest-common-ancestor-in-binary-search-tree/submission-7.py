# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ##Recursive but is binary tree not BST: (won't run in this ide)
        # if not root:
        #     return None

        # if root == p or root == q:
        #     return root
        
        # lContains = self.lowestCommonAncestor(root.left, p, q)
        # rContains = self.lowestCommonAncestor(root.right, p, q)

        # if lContains and rContains:
        #     return root
        

        # return rContains or lContains





        ##Recursive
        # if not root or not p or not q:
        #     return None
        
        # if max(p.val, q.val) < root.val:
        #     return self.lowestCommonAncestor(root.left, p, q)
        
        # elif min(p.val, q.val) > root.val:
        #     return self.lowestCommonAncestor(root.right, p, q)
        
        # return root

        ##Iterative:

        qVal = q.val
        pVal = p.val

        while root:
            if root.val > max(qVal, pVal):
                root = root.left
            
            elif root.val < min(qVal, pVal):
                root = root.right
            
            else:
                return root
        


























        # while root:
        #     if root.val < p.val and root.val < q.val:
        #         root = root.right
        #     elif root.val > p.val and root.val > q.val:
        #         root = root.left
        #     else:
        #         return root

        