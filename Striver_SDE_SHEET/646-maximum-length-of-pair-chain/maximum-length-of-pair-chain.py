class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: (x[1],x[0]))
        prev = pairs[0][1]
        count = 0
        ans = 0
        for i,j in pairs:
            if prev<i:
                count+=1
                prev = j
                ans = max(ans,count)
        return ans+1