class Solution:
    def coloredCells(self, n: int) -> int:
        return (((n-1)**2)<<1)+(2*n-1)


