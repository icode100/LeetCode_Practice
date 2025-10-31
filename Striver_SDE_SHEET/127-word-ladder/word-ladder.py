class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque([(beginWord,0)])
        vis = {beginWord}
        N = len(beginWord)
        check = set(wordList)
        while q:
            word,level = q.popleft()
            if word==endWord: return level+1
            for i in range(N):
                for c in 'qwertyuiopasdfghjklzxcvbnm':
                    newword = word[:i]+c+word[i+1:]
                    if newword not in vis and newword in check:
                        q.append((newword,level+1))
                        vis.add(newword)
        return 0



