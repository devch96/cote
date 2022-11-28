import sys
input = sys.stdin.readline
n, m = map(int,input().split())
trees = list(map(int,input().split()))
start = 1
end = max(trees)
while start <= end:
    result = 0
    mid = end + ((start - end)//2)
    for i in trees:
        if i >= mid:
            result += i - mid
    if result >= m:
        start = mid +1
    else:
        end = mid - 1
print(end)
