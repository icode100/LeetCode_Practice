# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root: return 0
            l = dfs(root.left)
            r = dfs(root.right)
            return l+r+root.val
        
        total = dfs(root)
        self.ans = 0
        self.mod = int(1e9+7)
        def dfs2(root):
            if not root: return 0
            l = dfs2(root.left)
            r = dfs2(root.right)
            currentsum = l+r+root.val
            posans = (currentsum*(total-currentsum))
            if posans>self.ans:
                self.ans = posans
            return currentsum
        dfs2(root)
        return self.ans%self.mod
