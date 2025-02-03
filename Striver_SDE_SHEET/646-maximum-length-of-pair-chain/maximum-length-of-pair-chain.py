class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        prev = pairs[0][1]
        count = 0
        ans = 0
        for i,j in pairs:
            if prev<i:
                count+=1
                prev = j
                ans = max(ans,count)
            else:
                prev = min(prev,j)
        return ans+1