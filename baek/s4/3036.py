#링
import sys
input = sys.stdin.readline
n = int(input())
ring = list(map(int,input().split()))
def gcd(x,y):
    while y:
        x,y = y, x%y
    return x
std = ring[0]*2
for i in range(1,n):
    denominator = ring[i]*2
    numerator = std
    measure = gcd(denominator, numerator)
    answer = '{nume}/{deno}'.format(nume = numerator//measure, deno = denominator//measure)
    print(answer)