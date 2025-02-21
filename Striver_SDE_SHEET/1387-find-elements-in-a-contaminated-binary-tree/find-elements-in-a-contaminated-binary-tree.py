# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        q = deque([root])
        self.hashset = {root.val}
        while q:
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                self.hashset.add(node.val)
                if node.left: 
                    node.left.val = node.val*2+1
                    q.append(node.left)
                if node.right:
                    node.right.val = node.val*2+2
                    q.append(node.right)
        
    def find(self, target: int) -> bool:
        return target in self.hashset


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)