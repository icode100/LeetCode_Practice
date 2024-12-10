class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s==t: return s
        if len(s)<len(t): return ""
        def check(temp,counter):
            for key,val in counter.items():
                if key not in temp or counter[key]>temp[key]:
                    return False
            return True
        counter_t = Counter(t)
        left = 0
        right = 0
        n = len(s)
        ans = str()
        temp_hash = defaultdict(int)
        min_length = n
        while right<n:
            temp_hash[s[right]]+=1
            while check(temp_hash,counter_t):
                if right-left+1<=min_length:
                    min_length = right-left+1
                    ans = s[left:right+1]
                temp_hash[s[left]]-=1
                if temp_hash[s[left]]==0: temp_hash.pop(s[left])
                left+=1
            right+=1
        return ans

                