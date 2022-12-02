import sys
input = sys.stdin.readline
n, m = map(int,input().split())
site = dict()
for _ in range(n):
    s = input().split()
    site[s[0]] = s[1]
for _ in range(m):
    print(site[input().rstrip()])