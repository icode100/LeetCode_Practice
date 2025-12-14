class Solution:
    def __init__(self):
        self.mod = int(1e9+7)
    def numberOfWays(self, corridor: str) -> int:
        N:int = len(corridor)

        count:int = 0
        ans:int = 1
        i:int = 0
        if corridor.count('S') == 0 or corridor.count('S') % 2 != 0:
            return 0
        target = corridor.count('S')//2
        
        while i<N:
            if corridor[i]=='S':
                count+=1
            if count==2:
                target-=1
                i+=1
                temp = 0
                while i<N and corridor[i]=='P':
                    temp+=1
                    i+=1
                if target>0: ans = (ans*(temp+1))%self.mod
                count = 0
                continue
            i+=1

        return ans
