class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        n = -1
        counter = defaultdict(lambda:defaultdict(int))
        for num in nums:
            strnum = str(num)
            if n==-1: n=len(strnum)
            for i,c in enumerate(strnum): 
                counter[i][int(c)]+=1
        # print(counter)
        ans = 0
        for i in range(n):
            for j in range(10):
                for k in range(j+1,10):
                    ans+=counter[i][j]*counter[i][k]
        return ans
