class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n==0:
            return len(tasks)
        c = Counter(tasks)
        counter = sorted([[i,c[i]] for i in c],key=lambda x:-x[1])
        mx = counter[0][1]   
        ans = (n+1)*(mx-1)
        for item in counter:
            if item[1]==mx:
                ans+=1
        return max(ans,len(tasks))

                





