class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # find with every character there is a substring that ends
        l,r,n = 0,0,len(s)
        hashing = defaultdict(int)
        result = 0
        while r<n:
            hashing[s[r]]+=1
            while len(hashing)==3:
                print("hi")
                result+=(n-r-1)
                result+=1
                hashing[s[l]]-=1
                if hashing[s[l]]==0:
                    hashing.pop(s[l])
                l+=1
            r+=1
        return result

            