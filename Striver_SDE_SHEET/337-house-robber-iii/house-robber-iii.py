# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def recursion(root):
            if not root: return 0
            return max(
                recursion(root.left)+recursion(root.right),
                root.val+(recursion(root.left.left)+recursion(root.left.right) if root.left else 0)+ (recursion(root.right.right)+recursion(root.right.left) if root.right else 0)
            )
        return recursion(root)