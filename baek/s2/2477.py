#참외밭
import sys
input = sys.stdin.readline
k = int(input())
board = [input().split() for _ in range(6)]
dir = [int(v[0]) for v in board]
lengths = [int(v[1]) for v in board]
maxS , minS = [],[]
for i in range(1,5):
    if dir.count(i) == 1:
        maxS.append(lengths[dir.index(i)])
        temp = dir.index(i) + 3
        temp %= 6
        minS.append(lengths[temp])

print(k * ((maxS[0]*maxS[1]) - (minS[0]*minS[1])))
