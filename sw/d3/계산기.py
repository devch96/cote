import sys
input = sys.stdin.readline
T = int(input())
for i in range(1,T+1):
    n = int(input())
    nums = list(map(int,input().split()))
    result = 0
    for num in nums:
        if result == 0 or result == 1:
            result += num
        elif num == 0:
            result += num
        else:
            result *= num
    print(f'#{i} {result}')