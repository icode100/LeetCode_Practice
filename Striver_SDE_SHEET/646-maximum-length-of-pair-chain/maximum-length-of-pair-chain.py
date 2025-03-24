class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[-1])
        count = 0
        prev = pairs[0][1]
        for s,e in pairs[1:]:
            if s>prev:
                count+=1
                prev = e
        return count+1
