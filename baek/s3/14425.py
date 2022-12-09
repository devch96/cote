#문자열 집합
import sys
input = sys.stdin.readline
n , m = map(int,input().split())
s = set()
for _ in range(n):
    s.add(input().rstrip())
cnt = 0
for _ in range(m):
    if input().rstrip() in s:
        cnt += 1
print(cnt)