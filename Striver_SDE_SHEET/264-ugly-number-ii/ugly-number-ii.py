class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = SortedSet([1])
        ans = 0
        while n:
            ans = heap[0]
            heap.remove(ans)
            n-=1
            if not n: return ans
            for i in [2,3,5]:
                heap.add(ans*i)
            
        return ans
