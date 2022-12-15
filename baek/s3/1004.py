#어린 왕자
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    x1,y1,x2,y2 = map(int,input().split())
    n = int(input())
    cnt = 0
    for _ in range(n):
        cx,cy,cr = map(int,input().split())
        dis1 = (x1-cx)**2 + (y1-cy)**2
        dis2 = (x2-cx)**2 + (y2-cy)**2
        pow_cr = cr**2
        if (dis1 < pow_cr and dis2 > pow_cr) or (dis1>pow_cr and dis2<pow_cr):
            cnt += 1
    print(cnt)
