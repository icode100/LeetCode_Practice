# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue = deque([root])
        ans = list()
        flag = True
        while queue:
            N = len(queue)
            temp = [0]*N
            for i in range(N):
                node = queue.popleft()
                if flag: temp[i] = node.val
                else: temp[N-i-1] = node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            flag = not flag
            ans.append(temp.copy())
        return ans
