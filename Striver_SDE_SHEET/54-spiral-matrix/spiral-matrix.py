class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        vis = set()
        ans = list()
        endcol = len(mat[0])-1
        endrow = len(mat)-1
        strow = 0
        stcol = 0
        while strow <= endrow and stcol<=endcol:
            i = strow
            j = stcol
            while j<=endcol:
                if (i,j) in vis:
                    break
                ans.append(mat[i][j])
                vis.add((i,j))
                j+=1
            
            i = strow+1
            j = endcol
            while i<=endrow:
                if (i,j) in vis:
                    break
                ans.append(mat[i][j])
                vis.add((i,j))
                i+=1
            
            i = endrow
            j = endcol-1
            while j>=stcol:
                if (i,j) in vis:
                    break
                ans.append(mat[i][j])
                vis.add((i,j))
                j-=1
            
            i = endrow-1
            j = stcol
            while i>strow:
                if (i,j) in vis:
                    break
                ans.append(mat[i][j])
                vis.add((i,j))
                i-=1
            
            strow+=1
            endrow-=1
            stcol+=1
            endcol-=1
        return ans

