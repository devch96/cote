import sys
input = sys.stdin.readline
t = int(input())
temp = [0] * 11
temp[1] = 1
temp[2] = 2
temp[3] = 4
for i in range(4,11):
    temp[i] = sum(temp[i-3:i])
for _ in range(t):
    print(temp[int(input())])