from collections import deque
def solution(maps):
    n , m = len(maps)-1, len(maps[0])-1 # 최대 범위 정하기
    dx = [0,0,-1,1]
    dy = [-1,1,0,0] # 상하좌우 방향
    q = deque()
    q.append([0,0]) # 큐에 시작위치 삽입

    while q:
        x,y = q.popleft()
        for i in range(4): # 상하좌우 방향
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<=n and 0<=ny<=m and maps[nx][ny] == 1: # 범위를 벗어나지 않고 길이 안막혀있으면
                maps[nx][ny] = maps[x][y] + 1 # 기존에 움직인 횟수 + 1
                q.append([nx,ny])
    
    destination = maps[n][m]
    
    return destination if destination != 1 else -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))