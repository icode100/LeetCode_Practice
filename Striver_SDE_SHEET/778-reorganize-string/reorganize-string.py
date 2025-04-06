class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        heap = [(-v,k) for k,v in counter.items()]
        heapify(heap)
        string = ""
        while heap:
            temp = list()
            while string and heap and heap[0][1]==string[-1]:
                temp.append(heappop(heap))
            if temp and not heap: return ""
            v,k = heappop(heap)
            string+=k
            if v+1<0: heappush(heap,(v+1,k))
            while temp: heappush(heap,temp.pop())
        return string
