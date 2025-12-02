class Solution:
    def __init__(self):
        self.int_max = sys.maxsize
        self.int_min = -sys.maxsize-1
        self.mod = int(1e9+7)

    def countTrapezoids(self, points: List[List[int]]) -> int:
        hashy = defaultdict(lambda : (0,0))

        for x,y in points:
            cnt,lines = hashy[y]
            if cnt==0: hashy[y] = (1,0)
            elif cnt==1: hashy[y] = (2,1)
            else:
                hashy[y] = (cnt+1,(cnt+lines))

        total = sum(hashy[y][1] for y in hashy) % self.mod

        ans = 0
        for y in hashy:
            numLines = hashy[y][1]
            ans += ((total - numLines) * numLines) % self.mod
            total-=numLines

        return ans%self.mod

        


        