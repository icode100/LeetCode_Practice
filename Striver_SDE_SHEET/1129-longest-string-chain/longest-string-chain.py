class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = lambda x: len(x))
        N = len(words)
        dp = [1]*N
        def check(w1, w2):
            if len(w2) != len(w1) + 1:
                return False
            i1, i2 = 0, 0
            mismatch = 0
            while i1 < len(w1) and i2 < len(w2):
                if w1[i1] == w2[i2]:
                    i1 += 1
                    i2 += 1
                else:
                    mismatch += 1
                    i2 += 1
                    if mismatch > 1:
                        return False
            return True
        for i in range(N):
            for j in range(i):
                if check(words[j],words[i]):
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)


