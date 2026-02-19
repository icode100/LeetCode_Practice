# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return  None
        leftend = self.flatten(root.left)
        rightend = self.flatten(root.right)
        if leftend:
            temp = root.right
            root.right = root.left
            leftend.right = temp
            root.left = None
        if rightend: return rightend
        if leftend: return leftend
        return root
        
        