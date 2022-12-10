import sys
input = sys.stdin.readline
n = int(input())
numlist = sorted([int(input()) for _ in range(n)])
interval = []
for i in range(1,n):
    interval.append(numlist[i] - numlist[i-1])

def GCD(x,y):
    while y:
        x, y = y, x % y
    return x

a = interval[0]
for idx in range(1, len(interval)):
    a = GCD(a,interval[idx])

answer = set()
answer.add(a)
for i in range(2,int(a**0.5)+1):
    if a % i == 0:
        answer.add(i)
        answer.add(a//i)
print(*sorted(list(answer)))