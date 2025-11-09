class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        distance = [int(1e9)]*n
        distance[src] = 0
        for _ in range(k+1):
            temp = distance.copy()
            for u,v,wt in flights:
                if distance[u] != int(1e9) and distance[u]+wt<distance[v]:
                    temp[v] = min(temp[v],distance[u]+wt)
            distance = temp
        return distance[dst] if distance[dst] != int(1e9) else -1                