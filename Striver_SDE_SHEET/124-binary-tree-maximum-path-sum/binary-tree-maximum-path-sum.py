# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.pathsum = -sys.maxsize
        def dfs(root):
            if not root: return 0
            leftsum = max(dfs(root.left),0)
            rightsum = max(dfs(root.right),0)
            self.pathsum = max(self.pathsum,leftsum+rightsum+root.val)
            return max(leftsum,rightsum)+root.val
        dfs(root)
        return self.pathsum