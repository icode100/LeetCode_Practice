class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def recursion(row,col):
            if row==m-1 and col==n-1:
                return 1
            if row==m-1:
                return 1
            if col==n-1:
                return 1
            bottom = recursion(row+1,col)
            right  = recursion(row,col+1)
            return bottom+right
        return recursion(0,0)
