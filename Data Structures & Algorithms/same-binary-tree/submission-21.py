# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    from collections import deque
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ##BFS:
        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            node1 = q1.popleft()
            node2 = q2.popleft()

            if not node1 and not node2:
                continue
            
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            q1.append(node1.left)
            q1.append(node1.right)
            q2.append(node2.left)
            q2.append(node2.right)

        return True






        ##Iterative DFS:
        # stack = [(p, q)]

        # while stack:
        #     node1, node2 = stack.pop()

        #     if not node1 and not node2:
        #         continue
            
        #     if not node1 or not node2 or node1.val != node2.val:
        #         return False
            
        #     stack.append((node1.right, node2.right))
        #     stack.append((node1.left, node2.left))

        # return True






        ##Recursive DFS
        # if not p and not q:
        #     return True
        
        # if p and q and p.val == q.val:
        #     return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        # return False
    
