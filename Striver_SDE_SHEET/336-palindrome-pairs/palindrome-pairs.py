class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        bookkeeping = dict()
        ans = list()
        for i,word in enumerate(words): bookkeeping[word] = i
        for i,word in enumerate(words):
            if word==word[::-1] and "" in bookkeeping and bookkeeping[""]!=i:
                j = bookkeeping['']
                ans.append([i,j])
                ans.append([j,i])
            if word[::-1] in bookkeeping and bookkeeping[word[::-1]]!=i:
                j = bookkeeping[word[::-1]]
                ans.append([i,j])
            for k in range(1,len(word)):
                pre = word[:k]
                if word[:k]==word[:k][::-1] and word[k:][::-1] in bookkeeping and bookkeeping[word[k:][::-1]]!=i:
                    j = bookkeeping[word[k:][::-1]]
                    ans.append([j,i])
                if word[k:]==word[k:][::-1] and word[:k][::-1] in bookkeeping and bookkeeping[word[:k][::-1]]!=i:
                    j = bookkeeping[word[:k][::-1]]
                    ans.append([i,j])
        return ans