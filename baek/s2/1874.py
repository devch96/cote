import sys
input = sys.stdin.readline
t = int(input())
lt = [int(input()) for _ in range(t)]
temp = []
answer = []
boolean = True
flag = 1
for i in lt:
    while flag <= i:
        temp.append(flag)
        answer.append("+")
        flag += 1
    if temp[-1] == i:
        temp.pop()
        answer.append("-")
    else:
        boolean = False
if not boolean:
    print("NO")
else:
    for x in answer:
        print(x)
    