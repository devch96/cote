def solution(board):
    n = len(board)
    move = [(-1,0),(1,0),(0,-1),(0,1),(1,1),(1,-1),(-1,1),(-1,-1)]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for x, y in move:
                    if i+x not in range(n):
                        continue
                    if j+y not in range(n):
                        continue
                    if board[i+x][j+y] == 1:
                        continue
                    board[i+x][j+y] = -1

    answer = 0
    for a in board:
        answer += a.count(0)

    return answer
