# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @cache
        def recursion(start,end):
            if start>end: return [None]
            ans = list()
            for i in range(start,end+1):
                leftt = recursion(start,i-1)
                rightt = recursion(i+1,end)
                for l in leftt:
                    for r in rightt:
                        ans.append(TreeNode(i,l,r))
            return ans
        return recursion(1,n)
                        