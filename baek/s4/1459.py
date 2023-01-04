#걷기
import sys
input = sys.stdin.readline
x,y,w,s = map(int,input().split())
ans1 = min(x,y)*s + abs(x-y)*w
if (x+y) % 2 == 0:
    ans2 = max(x,y)*s
else:
    ans2 = (max(x,y)-1)*s + w
ans3 = (x+y)*w
print(min(ans1,ans2,ans3))