# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        hashmap = defaultdict(int)
        q = deque([(root,0)])
        
        while q:
            N = len(q)
            for _ in range(N):
                node,x = q.popleft()
                hashmap[x] = node.val
                if node.left: q.append((node.left,x+1))
                if node.right: q.append((node.right,x+1))
        return [hashmap[k] for k in sorted(hashmap.keys())]