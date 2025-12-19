class DSU:
    def __init__(self,N:int)->None:
        self.parent:List[int] = [i for i in range(N)]
        self.size:List[int] = [1 for i in range(N)]

    def find(self,u:int)->int:
        if self.parent[u] == u: return u
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self,u:int,v:int)->bool:
        ultu:int
        ultv:int
        ultu,ultv = self.find(u), self.find(v)

        if ultu==ultv: return False

        if self.size[ultu] <= self.size[ultv]:
            self.parent[ultu] = ultv
            self.size[ultv]+=self.size[ultu]
        else:
            self.parent[ultv] = ultu
            self.size[ultu]+=self.size[ultv]
        
        return True


class Solution:
    def findAllPeople(self, N: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        dsu:DSU = DSU(N)
        timeMap:DefaultDict[int,List[Tuple[int,int]]] = defaultdict(list)
        for u,v,t in meetings:
            timeMap[t].append((u,v))

        dsu.union(firstPerson,0)

        for time in sorted(timeMap.keys()):
            tempSet:Set[int] = set()
            for u,v in timeMap[time]:
                dsu.union(u,v)
                tempSet.add(u)
                tempSet.add(v)

            for u in tempSet:
                if dsu.find(u)!=dsu.find(0):
                    dsu.parent[u] = u
                    dsu.size[u] = 1
        
        ans:List[int] = list()
        for i in range(N):
            if dsu.find(i)==dsu.find(0):
                ans.append(i)
        
        return ans

        
    