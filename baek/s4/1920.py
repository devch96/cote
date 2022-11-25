t = int(input())
lt = set(list(map(int,input().split())))
n = int(input())
nlt = list(map(int,input().split()))
for i in nlt:
    if i in lt:
        print(1)
    else:
        print(0)