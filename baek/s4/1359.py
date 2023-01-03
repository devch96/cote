#복권
import sys
from math import comb
input = sys.stdin.readline
n,m,k = map(int,input().split())
acc = 1
p = comb(n,m)
ans = 0
while m >= k :
    if (n-m < m-k):
        k+=1
        continue
    acc = comb(m,k) * comb(n-m,m-k)
    ans += acc/p
    k += 1
print(ans)