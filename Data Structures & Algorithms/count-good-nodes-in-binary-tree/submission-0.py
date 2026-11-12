# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ##perform DFS, keep a global stack variable
        ##each level, add max (top of stack, curr.val) to stack
        ##when we bounce up, pop top

        self.stack = []
        #[2 2
        self.result = 0

        def dfs(curr):
            if not curr:
                return None
            
            if len(self.stack):
                if curr.val >= self.stack[-1]:
                    self.result += 1
                self.stack.append(max(self.stack[-1], curr.val))
            else:
                self.result += 1
                self.stack.append(curr.val)

            dfs(curr.left)
            dfs(curr.right)
            self.stack.pop()
            return None
        
        dfs(root)

        return self.result
        