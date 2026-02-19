# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        current = root
        ans = list()
        while current:
            if not current.left:
                ans.append(current.val)
                current = current.right
            else:
                ptr = current.left
                while ptr.right and ptr.right!=current:
                    ptr = ptr.right
                
                if ptr.right==None:
                    ptr.right=current
                    current = current.left
                else:
                    ptr.right = None
                    ans.append(current.val)
                    current = current.right

        return ans
