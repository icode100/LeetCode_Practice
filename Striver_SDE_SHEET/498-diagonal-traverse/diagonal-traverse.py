class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m,n = len(mat),len(mat[0])
        flag = False
        stack = list()
        ans = list()
        def fx(sr,sc):
            nonlocal flag
            while 0<=sr<m and 0<=sc<n:
                if flag: ans.append(mat[sr][sc])
                else: stack.append(mat[sr][sc])
                sr+=1
                sc-=1
            flag = not flag
            while stack: ans.append(stack.pop())
        for j in range(n):
            sr,sc = 0,j
            fx(sr,sc)
        for j in range(1,m):
            sr,sc = j,n-1
            fx(sr,sc)
        return ans
