#토마토
import sys
from collections import deque
input = sys.stdin.readline
m,n = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
ans = 0
def bfs():
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                q.append((i,j))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))
bfs()
for x in graph:
    for y in x:
        if y == 0:
            print(-1)
            exit(0)
    ans = max(ans,max(x))
print(ans-1)