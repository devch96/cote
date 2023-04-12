#오큰수
import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
result = [-1] * n
stack = []
for i in range(n):
    while stack and a[stack[-1]] < a[i]:
        result[stack.pop()] = a[i]
    stack.append(i)
print(*result)
