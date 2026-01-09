# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        * basically the LCA of the deepest nodes
        * in general deepest nodes have same height
        * so if left height and right height for a node are the same then it might be potential root else which ever side is max
        '''
        def dfs(root):
            if not root: return [0,None]
            l,ln = dfs(root.left)
            r,rn = dfs(root.right)
            if l==r: return [l+1,root]
            return [max(l,r)+1, ln if l>r else rn]
        
        return dfs(root)[1]