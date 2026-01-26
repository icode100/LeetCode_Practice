class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = inf
        N = len(arr)
        res = list()
        for i in range(N-1):
            ans = min(ans,abs(arr[i]-arr[i+1]))
        
        for i in range(N-1):
            if abs(arr[i]-arr[i+1])==ans:
                res.append([arr[i],arr[i+1]])

        return res