from collections import deque
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        if not tokens:
            return 0
        max_score = 0
        q = deque(sorted(tokens))
        if power<q[0]:
            return 0
        faceup = True
        score = 0
        while q:
            if faceup:
                score+=1
                max_score = max(score,max_score)
                power-=q.popleft()
                if q:
                    faceup = False if power<q[0] else True
            else:
                score-=1
                max_score = max(score,max_score)
                power+=q.pop()
                if q:
                    faceup = False if power<q[0] else True
        return max_score


