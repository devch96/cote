import sys
input = sys.stdin.readline
n = int(input())
card = set(list(map(int,input().split())))
m = int(input())
prob = list(map(int,input().split()))
for i in prob:
    print(1 if i in card else 0 , end=" ")