import sys
input = sys.stdin.readline
def palin(str, l, r):
    global cnt
    cnt += 1
    if l >= r:
        return 1
    elif str[l] != str[r]:
        return 0
    else:
        return palin(str,l+1,r-1)
def isPalin(str):
    return palin(str,0,len(str)-1)
n = int(input())
for _ in range(n):
    cnt = 0
    print(isPalin(input().rstrip()), cnt)