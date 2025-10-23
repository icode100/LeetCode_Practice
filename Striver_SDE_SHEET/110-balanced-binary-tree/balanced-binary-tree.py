# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root: return 0
            leftd,rightd = dfs(root.left),dfs(root.right)
            if leftd==-1 or rightd==-1: return -1
            if abs(leftd-rightd)>1: 
                return -1
            return max(leftd,rightd)+1
        return bool(dfs(root)+1)
            
