# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = list()
        ptr = root
        while ptr:
            self.stack.append(ptr)
            ptr = ptr.left
    def next(self) -> int:
        node = self.stack.pop()
        if node.right:
            ptr = node.right
            while ptr:
                self.stack.append(ptr)
                ptr = ptr.left
        return node.val
    def hasNext(self) -> bool:
        if not self.stack: 
            return False
        return True
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()