import sys
input = sys.stdin.readline
n,m,b = map(int,input().split())
ground = [list(map(int,input().split())) for _ in range(n)]
answer = int(1e9)
tall = 0
for i in range(257):
    max = 0
    min = 0
    for x in range(n):
        for y in range(m):
            if ground[x][y] >= i:
                max += (ground[x][y]-i)
            else:
                min += (i - ground[x][y])
    if max + b >= min:
        if min + (max*2) <= answer:
            answer = min + (max*2)
            tall = i
print(answer, tall)
