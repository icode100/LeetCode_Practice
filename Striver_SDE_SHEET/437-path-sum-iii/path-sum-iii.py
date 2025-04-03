# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        hashmap,count = defaultdict(int),0
        def dfs(root,current):
            nonlocal count
            if not root: return 0
            current += root.val
            if current==targetSum: count+=1
            count+=hashmap[current-targetSum]
            hashmap[current]+=1
            dfs(root.left,current)
            dfs(root.right,current)
            hashmap[current]-=1
        dfs(root,0)
        return count

