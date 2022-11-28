import sys
input = sys.stdin.readline
t = int(input())
stack = []
for _ in range(t):
    n = int(input())
    if n != 0:
        stack.append(n)
    else:
        stack.pop()
print(sum(stack))