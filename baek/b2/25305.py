import sys
input = sys.stdin.readline
n,k = map(int,input().split())
score = sorted(list(map(int,input().split())), reverse = True)
print(score[k-1])
