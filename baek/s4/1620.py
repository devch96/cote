import sys
input = sys.stdin.readline
a, b = map(int,input().split())
dogam = {i : input().rstrip() for i in range(1,a+1)}
dogam1 = {v:k for k,v in dogam.items()}
for _ in range(b):
    q = input().rstrip()
    if q.isdigit():
        print(dogam.get(int(q)))
    else:
        print(dogam1.get(q))