#최소 힙
import sys
import heapq
input = sys.stdin.readline
n = int(input())
minheap = []
for _ in range(n):
    a = int(input())
    if a == 0:
        print(heapq.heappop(minheap) if minheap else 0)
    else:
        heapq.heappush(minheap, a)