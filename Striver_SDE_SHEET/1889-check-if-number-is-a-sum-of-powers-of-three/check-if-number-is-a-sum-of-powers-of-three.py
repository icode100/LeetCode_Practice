class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n:
            if n%3 not in {0,1}: return False
            n = n//3
        return True