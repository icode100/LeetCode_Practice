class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)
    def add(self, point: List[int]) -> None:
        x,y = point
        self.points[tuple(point)] += 1
    def count(self, point: List[int]) -> int:
        xq,yq = point
        ans = 0
        for x,y in self.points:
            if abs(xq-x)!=abs(yq-y) or x==xq or y==yq: continue
            if (x,yq) in self.points and (xq,y) in self.points: 
                ans += self.points[(x,yq)]*self.points[(xq,y)]*self.points[(x,y)]
        return ans



# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)