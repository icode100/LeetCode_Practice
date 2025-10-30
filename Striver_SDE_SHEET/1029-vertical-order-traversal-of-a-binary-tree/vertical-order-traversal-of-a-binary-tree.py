# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from heapq import *
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        hashmap = defaultdict(lambda: defaultdict(list))
        q.append((root,0,0))
        while q:
            n = len(q)
            for _ in range(n):
                node,col,row = q.popleft()
                heappush(hashmap[col][row],node.val)
                if node.left:q.append((node.left,col-1,row+1))
                if node.right:q.append((node.right,col+1,row+1))
        result = list()
        for col in sorted(hashmap.keys()):
            temp = list()
            for vals in hashmap[col].values():
                while vals:
                    temp.append(heappop(vals))
            result.append(temp.copy())
        return result
