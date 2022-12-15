#이항 계수 2
import sys
from math import factorial
input = sys.stdin.readline
n,k = map(int,input().split())
result = factorial(n)//(factorial(k) * factorial(n-k))
print(result % 10007)
