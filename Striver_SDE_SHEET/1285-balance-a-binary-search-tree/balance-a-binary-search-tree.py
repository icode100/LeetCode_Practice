# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder(root):
            if not root: return 
            inorder(root.left)
            inor.append(root)
            inorder(root.right)
        inor = list()
        inorder(root)

        def create(start,end):
            if start>end:
                return None
            
            mid = (start+end)//2
            leftsub = create(start,mid-1)
            rightsub = create(mid+1,end)
            return TreeNode(inor[mid].val,leftsub,rightsub)
        
        return create(0,len(inor)-1)