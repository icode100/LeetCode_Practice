# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def recursion(preorder,postorder):
            if len(preorder)==1 and len(postorder)==1: return TreeNode(preorder[0])
            
            print(preorder,postorder)
            root = TreeNode(preorder[0])
            rightnode = postorder[-2] 
            leftnode = preorder[1]
            idx = preorder.index(rightnode)
            idx2 = postorder.index(leftnode)
            if leftnode==rightnode:
                root.left = recursion(preorder[1:],postorder[:-1])
                root.right = None
                return root
            if idx==1:
                root.left = TreeNode(preorder[1])
                return root
            root.left = recursion(preorder[1:idx],postorder[:idx2+1])
            root.right = recursion(preorder[idx:],postorder[idx2+1:-1])
            return root
        return recursion(preorder,postorder)