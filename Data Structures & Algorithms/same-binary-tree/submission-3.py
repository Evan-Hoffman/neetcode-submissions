# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if not p or not q:
            return False

        stackP = [p]
        stackQ = [q]

        while (stackP and stackQ) and (len(stackP) == len(stackQ)):
            nodeP = stackP.pop()
            nodeQ = stackQ.pop()

            if nodeP.val != nodeQ.val:
                return False
            
            if nodeP.right and nodeQ.right:
                stackP.append(nodeP.right)
                stackQ.append(nodeQ.right)
            elif nodeP.right or nodeQ.right:
                return False

            if nodeP.left and nodeQ.left:
                stackP.append(nodeP.left)
                stackQ.append(nodeQ.left)
            elif nodeP.left or nodeQ.left:
                return False
        
        if len(stackP) != len(stackQ):
            return False
        
        return True
                
            


            

            

                




        