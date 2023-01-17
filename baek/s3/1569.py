import sys
input = sys.stdin.readline
t = int(input())
dot = list()
for _ in range(t):
    dot.append(list(map(int,input().split())))
dotx = list()
doty = list()
for x,y in dot:
    dotx.append(x)
    doty.append(y)
print(1 if max(dotx) - min(dotx) == max(doty) - min(doty) else 0)
