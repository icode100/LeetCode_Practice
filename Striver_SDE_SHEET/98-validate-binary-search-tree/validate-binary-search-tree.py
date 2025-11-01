# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recursion(root,min,max):
            if not root: return True
            return min<root.val<max and recursion(root.left,min,root.val) and recursion(root.right,root.val,max)
        return recursion(root,-inf,inf)

    #     class Solution:
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     def recursion(root, min_val, max_val): return True if not root else (min_val < root.val < max_val) and recursion(root.left, min_val, root.val) and recursion(root.right, root.val, max_val)
    #     return recursion(root, -float('inf'), float('inf'))