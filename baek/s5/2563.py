#색종이
import sys
input = sys.stdin.readline
board = [[0 for _ in range(101)] for _ in range(101)]
t = int(input())
for _ in range(t):
    x, y = map(int,input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            board[i][j] = 1
answer = 0
for x in board:
    answer += sum(x)
print(answer)