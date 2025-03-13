# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def recursion(root):
            if not root: return None
            l = recursion(root.left)
            r = recursion(root.right)
            if l:
                l.right = root.right
                root.right = root.left
                root.left = None
            if r: return r
            elif l: return l
            else: return root
        recursion(root)
