class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1: return [[1]]
        ans = [[1],[1,1]]
        if numRows==2: return ans
        for i in range(numRows-2):
            temp = []
            for j in range(i+3):
                if j==0 or j==i+2: temp.append(1)
                else: temp.append(ans[i+1][j]+ans[i+1][j-1])
            ans.append(temp)
        return ans
