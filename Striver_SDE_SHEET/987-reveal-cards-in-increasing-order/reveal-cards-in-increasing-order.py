from heapq import heapify, heappop
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        heapify(deck)
        n = len(deck)
        result = [-1 for i in range(n)]
        flag = True
        index_set = set(range(n))
        i = 0
        while len(index_set):
            i = min(index_set)
            print(i)
            while i<len(result):
                if flag and result[i]==-1:
                    result[i] = heappop(deck)
                    index_set.remove(i)
                    flag = not flag
                elif result[i]==-1: 
                    flag = not flag
                i+=1
            # flag = not flag
        return result