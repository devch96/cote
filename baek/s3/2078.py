#무한 이진 트리
import sys
input = sys.stdin.readline
a,b = map(int,input().split())
l = 0
r = 0
while a>1 and b>1:
    if a > b:
        l += a//b
        a%=b
    else:
        r += b//a
        b%=a
l += a-1
r += b-1
print(l,r)