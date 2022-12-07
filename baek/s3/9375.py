import sys
from collections import Counter
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    answer = 1
    wear = []
    a = int(input())
    for i in range(a):
        c, k = input().split()
        wear.append(k)
    wC = Counter(wear)
    for key in wC:
        answer *= wC[key] + 1
    print(answer-1)
