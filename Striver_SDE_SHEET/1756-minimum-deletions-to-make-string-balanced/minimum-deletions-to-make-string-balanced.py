class Solution:
    def minimumDeletions(self, s: str) -> int:
        # if 'a' not in s or 'b' not in s: return 0
        N = len(s)

        dp = [[inf,inf] for _ in range(N+1)]
        dp[N][0] = dp[N][1] = 0
        for index in range(N-1,-1,-1):
            for flag in [0,1]:
                if flag:
                    if s[index]=='b':
                        dont_flip = 1+dp[index+1][1]
                        flip = dp[index+1][0]
                        dp[index][flag] = min(flip,dont_flip)
                    else:
                        dont_flip = dp[index+1][1]
                        flip = 1+dp[index+1][0]
                        dp[index][flag] =  min(flip,dont_flip)
                else:
                    if s[index]=='b':
                        dp[index][flag] = dp[index+1][0]
                    else:
                        dp[index][flag] = 1+dp[index+1][0]
    
        return dp[0][1]
        # @cache
        # def recursion(index,flag):
        #     if index>=N:
        #         return 0
        #     if flag:
        #         if s[index]=='b':
        #             dont_flip = 1+recursion(index+1,True)
        #             flip = recursion(index+1,False)
        #             return min(flip,dont_flip)
        #         else:
        #             dont_flip = recursion(index+1,True)
        #             flip = 1+recursion(index+1,False)
        #             return min(flip,dont_flip)
        #     else:
        #         if s[index]=='b':
        #             return recursion(index+1,False)
        #         else:
        #             return 1+recursion(index+1,False)

        # return recursion(0,True)
