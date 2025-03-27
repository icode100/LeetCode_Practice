class Solution:
    def minDeletions(self, s: str) -> int:
        counter = sorted([[v,k] for k,v in Counter(s).items()], key = lambda x: -x[0])
        n = len(counter)
        currentmin = counter[0][0]
        ans = 0
        for i in range(1,n):
            if counter[i][0]==counter[i-1][0]:
                ans+=1
                counter[i][0]-=1
            elif counter[i][0]>currentmin:
                if currentmin > 0:
                    ans+=(counter[i][0]-currentmin+1)
                    counter[i][0] = currentmin-1
                else:
                    ans+=counter[i][0]
                    counter[i][0] = currentmin
            currentmin = min(currentmin,counter[i][0])
        # print(counter)
        return ans