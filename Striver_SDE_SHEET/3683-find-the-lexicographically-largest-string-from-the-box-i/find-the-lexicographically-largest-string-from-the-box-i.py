class Solution:
    def answerString(self, word: str, n: int) -> str:
        N = len(word)
        if n==1: return word
        ans = ""
        for i in range(N):
            ans = max(ans,word[i:min(i+N-n+1,N)])
        return ans