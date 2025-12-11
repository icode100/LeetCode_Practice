class Solution:
    def countCoveredBuildings(self, N: int, buildings: List[List[int]]) -> int:
        row_max:List[int] = [0]*(N+1)
        row_min:List[int] = [N+1]*(N+1)
        col_max:List[int] = [0]*(N+1)
        col_min:List[int] = [N+1]*(N+1)

        for x,y in buildings:
            x:int
            y:int

            row_max[y] = max(row_max[y],x)
            row_min[y] = min(row_min[y],x)

            col_max[x] = max(col_max[x],y)
            col_min[x] = min(col_min[x],y)

        count:int = 0
        for x,y in buildings: 
            x:int
            y:int

            if x>row_min[y] and x<row_max[y] and y<col_max[x] and y>col_min[x]:
                count += 1
        
        return count


                    
