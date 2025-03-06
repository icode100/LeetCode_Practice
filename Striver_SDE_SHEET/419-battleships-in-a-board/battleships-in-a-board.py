class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m,n = len(board),len(board[0])
        vis = set()
        count = 0
        for i in range(m):
            for j in range(n):
                if board[i][j]=='X' and (i,j) not in vis:
                    k = i
                    while k<m and board[k][j]=='X':
                        vis.add((k,j))
                        k+=1
                    k = j
                    while k<n and board[i][k]=='X':
                        vis.add((i,k))
                        k+=1
                    count+=1
        return count

                    