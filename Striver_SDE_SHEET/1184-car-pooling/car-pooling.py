class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        hashmap = defaultdict(int)
        for num,start,end in trips:
            hashmap[start]+=num
            hashmap[end]-=num
        current = 0
        for i in sorted(hashmap):
            current+=hashmap[i]
            if current>capacity:
                return False
        return True