class Solution:
    def maximumProfit(self, price: List[int], k: int) -> int:
        N:int = len(price)
        dp = [[[-inf,-inf,-inf] for _ in range(k+1)] for __ in range(N+1)]
        for i in range(N+1):
            dp[i][0][0] = 0
        
        for i in range(k+1):
            dp[N][i][0] = 0
        
        for index in range(N-1,-1,-1):
            for limit in range(1,k+1):
                for state in range(3):
                    noTran:int = dp[index+1][limit][state]
                    tran:int = -inf

                    if state == 0:
                        tran = max(tran, -price[index]+dp[index+1][limit][1], price[index]+dp[index+1][limit][2])
                    
                    elif state==1:
                        tran = max(tran, price[index]+dp[index+1][limit-1][0])
                    else:
                        tran = max(tran, -price[index]+dp[index+1][limit-1][0])
                    dp[index][limit][state] = max(tran, noTran)
        return dp[0][k][0]

        # @cache
        # def recursion(index:int, limit:int, state:int)->int:
        #     if limit==0: 
        #         return 0 if state==0 else -inf
        #     if index>=N:
        #         return 0 if state==0 else -inf

        #     noTran:int = recursion(index+1,limit, state)
        #     tran:int = -inf

        #     if state==0:
        #         tran = max(tran, -price[index]+recursion(index+1,limit,1), price[index]+recursion(index+1,limit,2))
                
        #     elif state==1:
        #         tran = max(tran, price[index]+recursion(index+1,limit-1,0))

        #     elif state==2:
        #         tran = max(tran,-price[index]+recursion(index+1,limit-1,0))

        #     return max(tran,noTran)
        
        # return recursion(0,k,0)
                


