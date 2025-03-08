# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q,ans = deque(),0
        q.append((root,0))
        while q:
            n = len(q)
            maxleft,maxright = inf,-inf
            for _ in range(n):
                node,i = q.popleft()
                maxleft,maxright = min(maxleft,i),max(maxright,i)
                if node.left: q.append((node.left,(2*i)+1))
                if node.right: q.append((node.right,(2*i)+2))
            ans = max(ans,maxright-maxleft+1)
        return ans
