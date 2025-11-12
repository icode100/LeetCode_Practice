# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        i = 0
        N = len(traversal)
        stack = list()
        root = None
        while i<N:
            level,num = 0,""
            while i<N and traversal[i]=='-':
                level+=1
                i+=1
            while i<N and traversal[i]!='-':
                num+=traversal[i]
                i+=1
            node = TreeNode(int(num))
            if level==0: root = node
            while stack and len(stack)>level:stack.pop()
            if stack and not stack[-1].left: stack[-1].left = node
            elif stack: stack[-1].right = node
            stack.append(node)
        return root