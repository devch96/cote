import sys
input = sys.stdin.readline
t = int(input())
stack = []
for i in range(t):
    s = input().strip()
    if s.startswith("push"):
        stack.append(s.split()[1])
    elif s == "pop":
        print(stack.pop() if stack else -1)
    elif s == "size":
        print(len(stack))
    elif s == "empty":
        print(0 if stack else 1)
    elif s == "top":
        print(stack[-1] if stack else -1)
