class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counter = Counter(tiles)
        def recursion():
            ans = 0
            for i in counter:
                if counter[i]!=0:
                    ans+=1
                    counter[i]-=1
                    ans+=recursion()
                    counter[i]+=1
            return ans
        return recursion()