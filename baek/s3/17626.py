import sys
input = sys.stdin.readline
n = int(input())
dp = [0,1]
for i in range(2, n+1):
    minV = 4
    for j in range(1, int(i**0.5)+1):
        minV = min(minV, dp[i-(j**2)])
    dp.append(minV+1)
print(dp[n])

#BRUTE_FORCE
# def fourSquares(n):
#     if int(n**0.5) == n**0.5:
#         return 1
#     for i in range(1,int(n**0.5) + 1):
#         if int((n - (i**2))**0.5) == (n-(i**2)**0.5):
#             return 2
#     for i in range(1, int(n**0.5)+1):
#         for j in range(1, int((n-i**2)**0.5)+1):
#             if int((n-i**2-j**2)**0.5) == (n-i**2-j**2)**0.5:
#                 return 3
#     return 4
