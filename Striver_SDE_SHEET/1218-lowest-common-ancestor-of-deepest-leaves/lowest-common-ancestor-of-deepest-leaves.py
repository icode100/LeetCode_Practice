# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node: return [0,None]
            lefth,leftnode = dfs(node.left)
            righth,rightnode = dfs(node.right)
            if lefth==righth: return [lefth+1,node]
            else: return [max(lefth,righth)+1, rightnode if righth>lefth else leftnode]
        return dfs(root)[1]




        