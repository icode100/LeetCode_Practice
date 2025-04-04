class Solution:
    def bestClosingTime(self, customers: str) -> int:
        N = len(customers)
        counter = Counter(customers)
        penalty = N
        yes,no,ans = 0,0,0
        for i in range(N+1):
            if no+counter['Y']-yes<penalty: ans,penalty = i,no+counter['Y']-yes
            if i<N: yes,no = yes+int(customers[i]=='Y'), no+int(customers[i]=='N')
        return ans
 