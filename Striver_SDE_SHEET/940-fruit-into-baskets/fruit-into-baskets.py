class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        N = len(fruits)
        checkset = defaultdict(int)
        l = 0
        ans = 0
        for r in range(N):
            checkset[fruits[r]]+=1
            while l<r and len(checkset)>2:
                checkset[fruits[l]]-=1
                if checkset[fruits[l]]==0: checkset.pop(fruits[l])
                l+=1
            ans = max(ans,r-l+1)
        return ans