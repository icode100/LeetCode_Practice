class Solution:
    def wordBreak(self, string: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        N = len(string)
        @cache
        def recursion(index):
            if index>=N:
                return True
            for i in range(index,N+1):
                if string[index:i+1] in words:
                    if recursion(i+1): return True
            return False
        return recursion(0)