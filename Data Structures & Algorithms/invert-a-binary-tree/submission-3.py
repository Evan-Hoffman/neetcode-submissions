# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    from collections import deque
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ## Recursive DFS:
        if not root:
            return None
        
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root




















        ## BFS:

        # if not root:
        #     return None
        
        # queue = deque()
        # queue.append(root)

        # while len(queue):

        #     for i in range(len(queue)):
        #         node = queue.popleft()
        #         temp = node.left
        #         node.left = node.right
        #         node.right = temp

        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        
        # return root


        ## Recursive DFS:
        # if not root:
        #     return None
        
        # temp = self.invertTree(root.left)
        # root.left = self.invertTree(root.right)
        # root.right = temp
        # return root

        #Iterative DFS:
        # if not root:
        #     return None

        # stack = [root]

        # while stack:
        #     node = stack.pop()
        #     temp = node.left
        #     node.left = node.right
        #     node.right = temp
        #     if node.left:
        #         stack.append(node.left)
        #     if node.right:
        #         stack.append(node.right)
        
        # return root

        

        