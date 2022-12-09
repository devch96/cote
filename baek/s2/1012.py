import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]
t = int(input())
def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if board[x][y] == 1:
        board[x][y] = 0
        for i in range(4):
            dfs(x + dx[i], y+dy[i])

        return True
    return False
for _ in range(t):
    m,n,k = list(map(int,input().split()))
    board = [[0]*m for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int,input().split())
        board[y][x] = 1
    cnt = 0
    for i in range(n):
        for j in range(m):
            if dfs(i,j):
                cnt += 1
    print(cnt)
