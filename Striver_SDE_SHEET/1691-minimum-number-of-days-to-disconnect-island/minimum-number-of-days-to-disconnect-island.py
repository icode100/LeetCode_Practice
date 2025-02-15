class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        vis = set()
        m,n = len(grid),len(grid[0])
        if 0 not in [grid[i][j] for i in range(m) for j in range(n)]: return 2
        bridges = 0
        timer = 0
        time_of_visit = defaultdict(int)
        lowest_time = defaultdict(int)
        def dfs(r,c,pr,pc):
            nonlocal bridges,timer
            vis.add((r,c))
            time_of_visit[(r,c)] = timer
            lowest_time[(r,c)] = timer
            timer+=1
            child = 0
            for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
                nr,nc = r+dr, c+dc
                if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]==1:
                    if (nr,nc)==(pr,pc): continue
                    if (nr,nc) not in vis:
                        dfs(nr,nc,r,c)
                        lowest_time[(r,c)] = min(lowest_time[(r,c)],lowest_time[(nr,nc)])
                        if lowest_time[(nr,nc)]>=time_of_visit[(r,c)] and (pr,pc)!=(-1,-1): bridges+=1
                        child+=1
                    else: lowest_time[(r,c)] = min(lowest_time[(r,c)],time_of_visit[(nr,nc)])
            if child>1 and (pr,pc)==(-1,-1): bridges+=1
        def number_of_components():
            count = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j]==1 and (i,j) not in vis: 
                        count+=1
                        dfs(i,j,-1,-1)
            return count
        num = number_of_components() 
        print(num,bridges,timer)
        if num==0 or num>1: return 0
        elif bridges>0: return 1
        elif timer==1: return 1
        else: return 2
        
        


