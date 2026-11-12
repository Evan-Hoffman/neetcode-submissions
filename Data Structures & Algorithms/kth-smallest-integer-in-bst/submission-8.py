# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.found = -1

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            self.k -= 1

            if self.k == 0:
                self.found = node.val
                return
            dfs(node.right)
        
        dfs(root)
        return self.found
        






















        
        ##Iterative DFS:
        # stack = []

        # if root:
        #     stack.append(root)
        
        # curr = root

        # while stack or curr:
        #     while curr:
        #         stack.append(curr)
        #         curr = curr.left
            
        #     curr = stack.pop()
        #     k -= 1
        #     if k == 0:
        #         return curr.val
            
        #     curr = curr.right












        ##Recursive DFS:
        # self.k = k
        # self.found = -1
        
        # def dfs(node):
        #     if not node:
        #         return
            
        #     dfs(node.left)
        #     self.k -=  1
        #     if self.k == 0:
        #         self.found = node.val
        #         return
        #     dfs(node.right)
        
        # dfs(root)
        # return self.found