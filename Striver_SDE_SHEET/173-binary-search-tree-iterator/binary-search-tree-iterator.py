# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.current = root

    def next(self) -> int:
        while self.current:
            if not self.current.left:
                node = self.current
                self.current = self.current.right
                return node.val
            else:
                ptr = self.current.left
                while ptr.right and ptr.right!=self.current:
                    ptr = ptr.right
                if ptr.right==None:
                    ptr.right = self.current
                    self.current = self.current.left
                else:
                    ptr.right = None
                    node = self.current
                    self.current = self.current.right
                    return node.val
        
    def hasNext(self) -> bool:
        return bool(self.current)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()