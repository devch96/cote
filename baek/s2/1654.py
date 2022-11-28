import sys
input = sys.stdin.readline
k, n = map(int,input().split())
lt = [int(input()) for _ in range(k)]
start, end = 1, max(lt)
while start <= end:
    mid = end + ((start-end)//2)
    cnt = 0
    for i in lt:
        cnt += i // mid
    if cnt >= n:
        start = mid+1
    else:
        end = mid -1
print(end)