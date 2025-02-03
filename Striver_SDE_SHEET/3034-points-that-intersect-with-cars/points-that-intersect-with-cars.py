class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        hashmap = defaultdict(int)
        maxidx = 0
        for start,end in nums:
            hashmap[start]+=1
            hashmap[end+1]-=1
            maxidx = max(maxidx,end)
        current,count = 0,0
        for i in range(maxidx+1):
            current+=hashmap[i]
            if current>0: count+=1
        return count
        
