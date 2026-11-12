# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        vals = []
        if not root:
            return vals

        q = deque([root])

        while q:
            vals.append(q[-1].val)

            for i in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return vals
























        # result = []
        # if not root:
        #     return result

        # q = deque([root])

        # while q:
        #     result.append(q[-1].val)
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)

        # return result
        
        