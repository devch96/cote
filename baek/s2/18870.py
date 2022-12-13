#좌표 압축
import sys
input = sys.stdin.readline
n = int(input())
x1 = list(map(int,input().split()))
x2 = sorted(list(set(x1)))
answer = {x2[i] : i for i in range(len(x2))}
for i in x1:
    print(answer[i], end=' ')