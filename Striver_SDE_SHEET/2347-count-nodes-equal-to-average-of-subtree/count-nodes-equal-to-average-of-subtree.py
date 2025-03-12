# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        valmap = {}
        summap = {}
        countmap = {}
        def sumcomp(root):
            if not root: return 0
            left = sumcomp(root.left)
            right = sumcomp(root.right)
            summap[root] = left+right+root.val
            return summap[root]
        def countcomp(root):
            if not root: return 0
            left = countcomp(root.left)
            right = countcomp(root.right)
            countmap[root] = 1+left+right
            return countmap[root]
        sumcomp(root)
        countcomp(root)
        q,ans = deque([root]),0
        while q:
            n = len(q)
            for _ in range(n):
                node = q.pop()
                if node.val==summap[node]//countmap[node]: ans+=1
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        return ans
