#날짜 계산
import sys
input = sys.stdin.readline
e,s,m = map(int,input().split())
e1,s1,m1 = 1,1,1
year = 1
while True:
    if e1 == e and s1 == s and m1 == m:
        break
    e1 += 1
    s1 += 1
    m1 += 1
    year += 1
    if e1 > 15:
        e1 = 1
    if s1 > 28:
        s1 = 1
    if m1 > 19:
        m1 = 1
print(year)