class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        # learn 2-d prefix sum
        N,M = len(mat),len(mat[0])
        prefix_matrix = [[0]*(M+1) for _ in range(N+1)]

        for i in range(1,N+1):
            for j in range(1,M+1):
                prefix_matrix[i][j] = prefix_matrix[i-1][j]+prefix_matrix[i][j-1]+mat[i-1][j-1]-prefix_matrix[i-1][j-1]
        
        def get_rect(i_s,j_s,i_e,j_e):
            return prefix_matrix[i_e][j_e]-prefix_matrix[i_s-1][j_e]-prefix_matrix[i_e][j_s-1]+prefix_matrix[i_s-1][j_s-1]

        l,r = 1,min(N,M)
        ans = 0
        while l<=r:
            mid = (l+r)//2
            if any(
                get_rect(i,j,i+mid-1,j+mid-1)<=threshold 
                for i in range(1,N-mid+2)
                for j in range(1,M-mid+2)
            ):
                ans = mid
                l = mid+1
            else:
                r = mid-1
        
        return ans
