class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        hashmap = defaultdict(int)
        for start,end in flowers:
            hashmap[start]+=1
            hashmap[end+1]-=1
        pos = list()
        prefix = list()
        sumi = 0
        for key in sorted(hashmap):
            pos.append(key)
            sumi+=hashmap[key]
            prefix.append(sumi)
        ans = list()
        for i in people:
            ans.append(prefix[bisect_right(pos,i)-1])
        return ans

        