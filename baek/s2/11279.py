#최대 힙
import sys
import heapq
input = sys.stdin.readline
n = int(input())
maxheap = []
for _ in range(n):
    a = int(input())
    if a == 0:
        print(heapq.heappop(maxheap)[1] if maxheap else 0)
    else:
        heapq.heappush(maxheap, (-a, a))