import sys
input = sys.stdin.readline
t = int(input())
lt = sorted(list(map(int,input().split())))
answer = 0
for i in range(t):
    answer+= lt[i] * (t-i)
print(answer)
