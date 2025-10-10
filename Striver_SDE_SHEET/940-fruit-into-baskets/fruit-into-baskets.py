class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # dikh raha hai sliding window hai karke
        hashset = defaultdict(int)
        ans,l = 0,0
        for r,fruit in enumerate(fruits):
            hashset[fruit]+=1
            while l<r and len(hashset)>2:
                hashset[fruits[l]]-=1
                if hashset[fruits[l]]==0: hashset.pop(fruits[l])
                l+=1
            ans = max(ans,r-l+1)
        return ans

        