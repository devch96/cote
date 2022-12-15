#이항 계수 2
import sys
from math import factorial
input = sys.stdin.readline
n,k = map(int,input().split())
result = factorial(n)//(factorial(k) * factorial(n-k))
print(result % 10007)

#dp
#파스칼의 삼각형
# dp = [[0] for i in range(10)]
# dp[1].append(1)
# for i in range(2,10):
#     for j in range(1,i+1):
#         if j == 1:
#             dp[i].append(1)
#         elif j == i:
#             dp[i].append(1)
#         else:
#             dp[i].append(dp[i-1][j-1] + dp[i-1][j])
# print(dp)
