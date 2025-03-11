class Solution:
    def distributeCookies(self, cookies: List[int], K: int) -> int:
        if len(cookies)==K: return max(cookies)
        hashmap = {k:0 for k in range(K)}
        max_val = -inf
        ans = int(1e8+1)
        n = len(cookies)
        def recursion(index):
            nonlocal max_val
            nonlocal ans
            if index==n:
                ans = min(ans,max_val)
                return 
            for i in range(K):
                hashmap[i]+=cookies[index]
                temp = max_val
                max_val = max(max_val,hashmap[i])
                recursion(index+1)
                max_val = temp
                hashmap[i]-=cookies[index]
        recursion(0)
        return ans



