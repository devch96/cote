#이중 우선순위 큐
import sys
import heapq
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    k = int(input())
    maxH = []
    minH = []
    visited = [False] * k
    for i in range(k):
        op, num = input().split()
        num = int(num)
        if op == 'I':
            heapq.heappush(maxH, (-num, i))
            heapq.heappush(minH, (num,i))
        else:
            if num == 1:
                while maxH and visited[maxH[0][1]]:
                    heapq.heappop(maxH)
                if maxH:
                    visited[maxH[0][1]] = True
                    heapq.heappop(maxH)
            else:
                while minH and visited[minH[0][1]]:
                    heapq.heappop(minH)
                if minH:
                    visited[minH[0][1]] = True
                    heapq.heappop(minH)
        while maxH and visited[maxH[0][1]]:
            heapq.heappop(maxH)
        while minH and visited[minH[0][1]]:
            heapq.heappop(minH)
    if not maxH or not minH:
        print("EMPTY")
    else:
        print(-maxH[0][0], minH[0][0])