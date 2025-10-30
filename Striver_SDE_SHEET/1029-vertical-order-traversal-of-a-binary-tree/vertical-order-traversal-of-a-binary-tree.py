# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        hashmap = defaultdict(lambda: defaultdict(lambda:SortedList()))
        q = deque([(root,0,0)])
        while q:
            N = len(q)
            for _ in range(N):
                node,x,y = q.popleft()
                hashmap[x][y].add(node.val)
                if node.left: q.append((node.left,x-1,y+1))
                if node.right: q.append((node.right,x+1,y+1))
        ans = list()
        for x in sorted(hashmap.keys()):
            temp = list()
            for y in sorted(hashmap[x].keys()):
                temp+=list(hashmap[x][y])
            ans.append(temp.copy())
        return ans

                





