class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap =  {'I':1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000 }
        
        N = len(s)
        ans = 0
        for i in range(N):
            if i<N-1 and hashmap[s[i]]<hashmap[s[i+1]]: ans-=hashmap[s[i]]
            else: ans+=hashmap[s[i]]
        return ans

                

            