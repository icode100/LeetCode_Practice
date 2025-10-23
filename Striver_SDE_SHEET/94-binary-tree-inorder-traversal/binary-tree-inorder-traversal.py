# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = list()
        stack = []
        ptr = root
        while ptr or stack:
            while ptr:
                stack.append(ptr)
                ptr = ptr.left
            ptr = stack.pop()
            ans.append(ptr.val)
            ptr = ptr.right
        return ans

