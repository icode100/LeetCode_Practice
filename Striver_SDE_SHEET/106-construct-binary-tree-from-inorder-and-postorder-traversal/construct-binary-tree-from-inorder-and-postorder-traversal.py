# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        hashmap = {inorder[i]:i for i in range(len(inorder))}
        n = len(inorder)
        def recursion(ps_,pe_,is_,ie_):
            if ps_>pe_ or is_>ie_:
                return None
            root = TreeNode(postorder[pe_])
            in_index = hashmap[postorder[pe_]]
            root.left = recursion(ps_,ps_+(in_index-is_)-1, is_,in_index-1)
            root.right = recursion(ps_+(in_index-is_), pe_-1, in_index+1,ie_)
            return root
        return recursion(0,n-1,0,n-1)
        