#N과 M (4)
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
num = []
def solution(start):
    if len(num) == m:
        print(*num)
        return
    for i in range(start,n+1):
        num.append(i)
        solution(i)
        num.pop()
solution(1)
