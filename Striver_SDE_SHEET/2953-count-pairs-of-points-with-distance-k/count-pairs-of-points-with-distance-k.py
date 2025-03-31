class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        hashmap = {}
        count = 0
        for x,y in coordinates:
            for i in range(k+1):
                xp,yp = x^i, y^(k-i)
                if (xp,yp) in hashmap: count+=hashmap[(xp,yp)]
            hashmap[(x,y)] = hashmap.get((x,y),0)+1
        return count

