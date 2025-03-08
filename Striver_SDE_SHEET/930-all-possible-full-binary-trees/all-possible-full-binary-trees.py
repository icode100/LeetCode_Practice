# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        @cache
        def recursion(n):
            if n==0: return []
            if n==1: return [TreeNode(0)]
            ans = list()
            for i in range(1,n,2):
                leftt = recursion(i)
                rightt = recursion(n-i-1)
                for l in leftt:
                    for r in rightt:
                        ans.append(TreeNode(0,l,r))
            return ans
        return recursion(n)
                        