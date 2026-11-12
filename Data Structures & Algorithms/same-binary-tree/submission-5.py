# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #Iterative DFS:
        stackP, stackQ = [p], [q]

        while stackP and stackQ:
            pNode = stackP.pop()
            qNode = stackQ.pop()

            if pNode and qNode:
                if pNode.val != qNode.val:
                    return False
                
                stackP.append(pNode.left)
                stackQ.append(qNode.left)
                stackP.append(pNode.right)
                stackQ.append(qNode.right)
            
            elif not pNode and not qNode:
                continue
            
            else:
                return False
        
        return True
            
            












        ##Recursive DFS
        # if not p and not q:
        #     return True
        
        # if (p and q) and (p.val == q.val):
        #     return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        # else:
        #     return False
       





















        # if not p and not q:
        #     return True
        
        # if (p and q) and (p.val == q.val):
        #     return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # else:
        #     return False