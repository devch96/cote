#조합 0의 개수
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
def countN(x,k):
    cnt = 0
    while x:
        x //= k
        cnt += x
    return cnt
        
five = countN(n,5) - countN(m,5) - countN(n-m,5)
two = countN(n,2) - countN(m,2) - countN(n-m,2)
print(min(five,two))