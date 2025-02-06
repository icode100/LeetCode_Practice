class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        array,ans = [0]*(n+1),0
        for i in range(n+1):array[max(0,i-ranges[i])] = max(array[max(0,i-ranges[i])], min(n,i+ranges[i]))
        best,next = array[0],0
        for i in range(n+1):
            if i>best: return -1
            if i==best:
                ans+=1
                next = max(next,array[i])
                best = next
                next = 0
            else: next = max(next,array[i])
        return ans