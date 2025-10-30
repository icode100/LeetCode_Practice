# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        hashmap = defaultdict(lambda: defaultdict(lambda:SortedList()))
        self.minx,self.maxx = inf,-inf
        def dfs(root,x,y):
            if not root: return 
            self.minx = min(self.minx,x)
            self.maxx = max(self.maxx,x)
            hashmap[x][y].add(root.val)
            dfs(root.left,x-1,y+1)
            dfs(root.right,x+1,y+1)
        dfs(root,0,0)
        ans = list()
        for i in range(self.minx,self.maxx+1):
            temp = list()
            for k in sorted(hashmap[i].keys()):
                temp+=list(hashmap[i][k])
            ans.append(temp.copy())
        return ans
                





