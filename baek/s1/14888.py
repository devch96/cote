import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int,input().split()))
plus, minus, multiple, divide = map(int,input().split())
maxV = int(-1e9)
minV = int(1e9)
def solution(depth, total):
    global maxV, minV
    global plus, minus, multiple, divide
    if depth == n:
        maxV = max(maxV, total)
        minV = min(minV, total)
    else:
        if plus > 0:
            plus -= 1
            solution(depth+1, total + data[depth])
            plus += 1
        if minus > 0:
            minus -= 1
            solution(depth+1, total - data[depth])
            minus += 1
        if multiple > 0 :
            multiple -= 1
            solution(depth+1, total * data[depth])
            multiple += 1
        if divide > 0 :
            divide -= 1
            solution(depth+1, int(total / data[depth]))
            divide += 1
solution(1, data[0])
print(maxV)
print(minV)