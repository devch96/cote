#좋은 구간
import sys
input = sys.stdin.readline
l = int(input())
s = list(map(int,input().split()))
n = int(input())
s.sort()
if n in s:
    print(0)
else:
    min = 0
    max = 0
    for a in s:
        if a < n:
            min = a
        elif a > n and max == 0:
            max = a
    max -= 1
    min += 1
    print((n-min)*(max-n+1) + (max-n))
