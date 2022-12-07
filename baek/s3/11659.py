import sys
input = sys.stdin.readline
n,t = map(int,input().split())
accu = [0] * (n+1)
temp = list(map(int,input().split()))
tmp = 0
for i in range(n):
    tmp += temp[i]
    accu[i+1] = tmp
for _ in range(t):
    start, end = map(int,input().split())
    print(accu[end] - accu[start-1])