import sys
input = sys.stdin.readline
A,B = map(str,input().split())
a = list(map(int,A))
b = list(map(int,B))
print(sum(a)*sum(b))