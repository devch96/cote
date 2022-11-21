N,M = map(int,input().split())
board = []
for i in range(N):
    board.append(list(input()))

board1 = list(zip(*board))
boardresult = 0
board1result = 0
for i in range(N):
    if board[i].count('.') == M:
        boardresult+=1
for i in range(M):
    if board1[i].count('.') == N:
        board1result += 1
print(max(boardresult,board1result))