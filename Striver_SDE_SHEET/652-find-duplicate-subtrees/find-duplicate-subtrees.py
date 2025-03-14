# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        hashset = {}
        ans = list()
        def recursion(root):
            if not root: return ''
            tree = f'{root.val},{recursion(root.left)},{recursion(root.right)}'
            hashset[tree] = hashset.get(tree,0)+1
            if tree in hashset and hashset[tree]==2: ans.append(root)
            return tree
        recursion(root)
        return ans