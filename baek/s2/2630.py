#색종이 만들기
import sys
input = sys.stdin.readline
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
result = []
def cut(x,y,n):
    color = paper[x][y]
    for i in range(x, x+n):
        for j in range(y,y+n):
            if color != paper[i][j]:
                cut(x,y,n//2)
                cut(x,y+n//2,n//2)
                cut(x+n//2,y,n//2)
                cut(x+n//2,y+n//2,n//2)
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)

cut(0,0,n)
print(result.count(0))
print(result.count(1))