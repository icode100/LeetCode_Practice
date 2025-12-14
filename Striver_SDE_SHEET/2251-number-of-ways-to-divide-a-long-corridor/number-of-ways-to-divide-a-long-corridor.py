class Solution:
    def __init__(self):
        self.mod = int(1e9+7)
    def numberOfWays(self, corridor: str) -> int:
        N:int = len(corridor)

        if corridor.count('S') % 2 != 0 or corridor.count('S') == 0:
            return 0
        dp = [[0,0,1] for _ in range(N+1)]
        for index in range(N-1,-1,-1):
            for seats in range(3):
                if seats==2:
                    if corridor[index]=='S': dp[index][seats] = dp[index+1][1] % self.mod
                    else: dp[index][seats] = (dp[index+1][0]+dp[index+1][2])%self.mod

                else:
                    if corridor[index]=='S': dp[index][seats] = dp[index+1][seats+1] % self.mod
                    else: dp[index][seats] = dp[index+1][seats] % self.mod
        
        return dp[0][0]
        # @cache
        # def recursion(index:int, seats:int)->int:
        #     if index==N: return 1 if seats==2 else 0

        #     if seats==2:
        #         if corridor[index]=='S': return recursion(index+1,1) % self.mod
        #         else: return (recursion(index+1,0)+recursion(index+1,2))%self.mod
            
        #     else:
        #         if corridor[index]=='S': return recursion(index+1,seats+1) % self.mod
        #         else: return recursion(index+1,seats) % self.mod

        
        # return recursion(0,0) % self.mod




