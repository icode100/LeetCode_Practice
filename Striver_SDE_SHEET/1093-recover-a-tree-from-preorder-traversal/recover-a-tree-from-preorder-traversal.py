# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = list()
        n = len(traversal)
        index = 0
        ans = None
        while index<n:
            level,string = 0,""
            while index<n and traversal[index]=='-': 
                level+=1
                index+=1
            while index<n and traversal[index]!='-': 
                string+=traversal[index]
                index+=1
            node = TreeNode(int(string))
            if level==0: ans = node
            while stack and len(stack)>level: stack.pop()
            if stack and not stack[-1].left:stack[-1].left = node
            elif stack: stack[-1].right = node
            stack.append(node)
        return ans
        

