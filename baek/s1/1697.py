import sys
from collections import deque
input = sys.stdin.readline
n,k = map(int,input().split())
M = 100000
check = [0] * 100001
def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(check[x])
            break
        for nx in [x-1, x+1, x*2]:
            if 0 <= nx <= M and not check[nx]:
                q.append(nx)
                check[nx] = check[x]+1

bfs()