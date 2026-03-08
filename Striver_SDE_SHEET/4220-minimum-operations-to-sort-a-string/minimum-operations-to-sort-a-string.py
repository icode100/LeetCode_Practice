class Solution:
    def minOperations(self, s: str) -> int:
        if s==''.join(sorted(s)): return 0
        if len(s)==2: return -1
        maxi,mini = max(s),min(s)
        # maxi_p,mini_p = max(s[1:]),mini(s[1:])
        # print(mini,maxi)
        if s[0]==mini or s[-1]==maxi:
            return 1
        if s[0]==maxi and s[-1]==mini: 
            if (s.index(mini)!=(len(s)-1)) or (maxi in s[1:]): return 2
            return 3
        return 2
