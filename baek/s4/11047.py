import sys
input = sys.stdin.readline
n, m = map(int,input().split())
coin = sorted([int(input()) for i in range(n)], reverse = True)
cnt = 0
print(coin)
for i in coin:
    if m == 0:
        break
    if m // i:
        cnt += m // i
        m -= (m//i)*i
print(cnt)