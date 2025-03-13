# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.parent = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node,p):
            if not node:
                return None
            node.parent = p
            dfs(node.left,node)
            dfs(node.right,node)
        dfs(root,None)
        ans = list()
        vis = set()
        def dfs2(node,k):
            if not node: return None
            vis.add(node)
            if k==0: ans.append(node.val)
            if node.left not in vis: dfs2(node.left,k-1)
            if node.right not in vis: dfs2(node.right,k-1)
            if node.parent not in vis: dfs2(node.parent,k-1)
        dfs2(target,k)
        return ans