class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        hashmap = defaultdict(int)
        for i,j in intervals:
            hashmap[i]+=1
            hashmap[j]-=1
        hashmap[newInterval[0]]+=1
        hashmap[newInterval[1]]-=1
        start,count,ans = 0,0, list()
        for i in sorted(hashmap):
            if count==0: start = i
            count+=hashmap[i]
            if count==0: ans.append((start,i))
        return ans