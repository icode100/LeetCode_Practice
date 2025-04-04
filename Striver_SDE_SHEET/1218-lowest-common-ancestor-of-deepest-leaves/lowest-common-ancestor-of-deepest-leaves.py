# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs1(node):
            if not node: return 0
            left = dfs1(node.left)
            right = dfs1(node.right)
            return max(left,right)+1
        maxdepth = dfs1(root)
        # print(maxdepth)
        def dfs(node,depth):
            if not node: return None
            if depth==maxdepth: return node
            left = dfs(node.left,depth+1)
            right = dfs(node.right,depth+1)
            if left and right: return node
            else: return left or right
        return dfs(root,1)




        