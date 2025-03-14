# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p,q = (p,q) if p.val<q.val else (q,p)
        between = lambda a,x,y: x<=a<=y
        def recursion(root):
            if not root: return None
            if between(root.val,p.val,q.val): return root
            elif root.val>q.val: return recursion(root.left)
            else: return recursion(root.right)
        return recursion(root)