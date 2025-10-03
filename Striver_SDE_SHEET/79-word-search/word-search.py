class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        stack = [word[i] for i in range(len(word))]
        N,M = len(board),len(board[0])
        def recursion(r,c,pathvis):
            if not stack: return True
            for dr,dc in [(-1,0),(0,-1),(1,0),(0,1)]:
                nr,nc = r+dr,c+dc
                if 0<=nr<N and 0<=nc<M and (nr,nc) not in pathvis and board[nr][nc]==stack[-1]:
                    temp = stack.pop()
                    pathvis.add((nr,nc))
                    if recursion(nr,nc,pathvis): return True
                    pathvis.remove((nr,nc))
                    stack.append(temp)
            return False
        for r in range(N):
            for c in range(M):
                if board[r][c]==stack[-1]:
                    elem = stack.pop()
                    if recursion(r,c,{(r,c)}): return True
                    stack.append(elem)

        return False



            