import sys
input = sys.stdin.readline
n,m = map(int,input().split())
d = {input().rstrip() for _ in range(n)}
b = {input().rstrip() for _ in range(m)}
db = d&b
print(len(db))
for i in sorted(list(db)):
    print(i)