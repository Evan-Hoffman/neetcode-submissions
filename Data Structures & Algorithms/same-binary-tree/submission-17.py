# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    from collections import deque
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ##Iterative DFS:
        if not p and not q:
            return True
        
        if not p or not q:
            return False

        pStack, qStack = [p], [q]

        while pStack and qStack:
            pNode, qNode = pStack.pop(), qStack.pop()

            if pNode.val != qNode.val:
                return False
            
            if pNode.left and qNode.left:
                pStack.append(pNode.left)
                qStack.append(qNode.left)
            
            if pNode.right and qNode.right:
                pStack.append(pNode.right)
                qStack.append(qNode.right)
            
            if (bool(pNode.left) != bool(qNode.left)) or (bool(pNode.right) != bool(qNode.right)):
                return False
        
        # if not pStack and not qStack:
        return True
        
        # return False








        ##Recursive DFS
        # if not p and not q:
        #     return True
        
        # if p and q and p.val == q.val:
        #     return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        # return False
    
