import sys
input = sys.stdin.readline
t = int(input())
tmp = []
for i in range(t):
    tmp.append(int(input()))
for i in sorted(tmp):
    print(i)