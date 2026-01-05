class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # simple stone transfer technique
        ans = 0
        minpos = int(1e9)
        neg = list()
        N = len(matrix)
        for i in range(N):
            for j in range(N):
                if matrix[i][j]<0:
                    neg.append(matrix[i][j])
                else: 
                    ans+=matrix[i][j]
                    minpos = min(minpos,matrix[i][j])
        
        if len(neg)&1==0:
            return ans+abs(sum(neg))
        else:
            tempsum = abs(sum(neg))
            print(tempsum,ans)
            maxneg = max(neg)
            tempsum+=(maxneg*2)
            if abs(maxneg)<minpos:
                return ans+tempsum
            else:
                tempsum+=(abs(maxneg)*2)
                return tempsum+ans-(minpos*2)