class Solution:
    def findReachable(self,towers, c, r):
        res = list()
        for x,y,q in towers:
            if abs(x-c[0])+abs(y-c[1]) <= r:
                res.append([x,y,q])
        
        return res

    def bestTower(self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:
        reachable = self.findReachable(towers,center,radius)
        reachable.sort(key = lambda x:(-x[2],x[0],x[1]))
        return [reachable[0][0],reachable[0][1]] if reachable else [-1,-1]