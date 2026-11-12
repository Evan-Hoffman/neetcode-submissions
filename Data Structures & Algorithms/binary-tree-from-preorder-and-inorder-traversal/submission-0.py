# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        ##the first value of preorder is going to be the root
        ##the values to the left of the root in inorder will be in the left subtree
        ##the values to the right of the root in inorder will be in the right subtree

        if not preorder and not inorder:
            return None
        
        root = TreeNode(val=preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[0:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root
        