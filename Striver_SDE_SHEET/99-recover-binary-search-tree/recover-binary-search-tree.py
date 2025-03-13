# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        first,second,prev = [None]*3
        def recursion(root):
            if not root: return None
            nonlocal first,second,prev
            recursion(root.left)
            if prev and prev.val>root.val:
                if not first: first,second = prev, root
                else: second = root
            prev = root
            recursion(root.right)
        recursion(root)
        first.val,second.val = second.val,first.val
        
