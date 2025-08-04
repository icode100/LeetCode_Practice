class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # dont fixate the algorithm before hand
        # each basket holds only one type of fruit
        # pick one fruit from everytree one fruit cannot be picked stop
        # have a mask for having the check only two kinds of fruits
        # pick and not pick
        # once we reach an invalid index we stop and also we should pick the fruit from every tree
        # another catch is we can start from any index
        # So its longest valid subarray
        hashset = {}
        N = len(fruits)
        ans = 0
        count = 0
        l=0
        for r in range(N):
            hashset[fruits[r]] = hashset.get(fruits[r],0)+1
            count+=1
            while len(hashset)>2:
                hashset[fruits[l]]-=1
                if hashset[fruits[l]]==0: hashset.pop(fruits[l])
                count-=1
                l+=1
            ans = max(count,ans)
        return ans

        