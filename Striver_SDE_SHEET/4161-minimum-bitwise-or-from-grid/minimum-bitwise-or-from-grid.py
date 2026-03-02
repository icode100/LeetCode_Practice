class Solution:
    def minimumOR(self, grid: List[List[int]]) -> int:
        ans = 0
        mask = 0
        for bit in range(31,-1,-1):
            testMask = mask | (1<<bit)
            possible = True
            for row in grid:
                found = False
                for val in row:
                    if not (val & testMask):
                        found = True
                        break
                if not found:
                    possible = False
                    break
            if possible:
                mask = testMask
            else:
                ans |= (1<<bit)
        return ans