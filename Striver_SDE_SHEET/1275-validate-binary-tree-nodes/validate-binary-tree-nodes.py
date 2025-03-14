class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        root = -1
        nodeset = set(leftChild) | set(rightChild)
        for i in range(n):
            if i not in nodeset:
                if root != -1: return False
                root = i
        print(root)
        q = deque()
        parent = set()
        q.append((root,-1))
        cnt = 0
        while q:
            x = len(q)
            for _ in range(x):
                node,p = q.popleft()
                cnt+=1
                if node in parent: return False
                parent.add(node)
                if leftChild[node]!=-1: q.append((leftChild[node],node))
                if rightChild[node]!=-1: q.append((rightChild[node],node))
        return True if cnt==n else False


