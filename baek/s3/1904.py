#01 타일
import sys
input = sys.stdin.readline
n = int(input())
dp = []
dp.append(1)
dp.append(2)
for i in range(2,n):
    dp.append((dp[i-1]+dp[i-2])%15746)
print(dp[n-1])