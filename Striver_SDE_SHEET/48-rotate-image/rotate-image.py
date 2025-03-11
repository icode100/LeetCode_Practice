class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for r in range(n//2):
            for c in range(n):
                matrix[r][c],matrix[n-r-1][c] = matrix[n-r-1][c], matrix[r][c]
        # for i in matrix: print(*i)
        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
        

        