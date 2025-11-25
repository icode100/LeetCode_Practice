class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        n = 1
        count = 1
        if k&1==0 or k%5==0: return -1
        while n%k!=0:
            n = (n*10)+1
            count+=1
        return count