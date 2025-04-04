# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recursion(root):
            if not root: return None
            if root==p or root==q: return root
            left = recursion(root.left)
            right = recursion(root.right)
            if left and right: return root
            if not left: return right
            if not right: return left
        return recursion(root)
