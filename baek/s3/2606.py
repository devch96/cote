from collections import deque
import sys
input = sys.stdin.readline
com = int(input())
t = int(input())
graph = [[] for i in range(com+1)]
visited = [0] * (com+1)
for i in range(t):
    a,b = map(int,input().split())
    graph[a] += [b]
    graph[b] += [a]
visited[1] = 1
#BFS
# q = deque([1])
# while q:
#     c = q.popleft()
#     for n in graph(c):
#         if visited[n] == 0:
#             q.append(n)
#             visited[n] = 1
# print(sum(visited) - 1)

#DFS
def dfs(n):
    visited[n] = 1
    for i in graph[n]:
        if visited[i] == 0:
            dfs(i)
dfs(1)
print(sum(visited) - 1)