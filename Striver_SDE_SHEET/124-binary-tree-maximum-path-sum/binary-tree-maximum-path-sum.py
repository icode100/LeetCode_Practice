# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self): self.ans = -inf
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root: return 0
            lefth,righth = max(0,dfs(root.left)),max(0,dfs(root.right))
            self.ans = max(self.ans,lefth+righth+root.val)
            return max(lefth,righth)+root.val
        dfs(root)
        return self.ans