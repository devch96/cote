#제곱 ㄴㄴ 수
import sys
input = sys.stdin.readline
def rootss(a,b):
    cnt = 0
    for i in range(a,b+1):
        if i == 1 or i==2:
            cnt += 1
        else:
            for j in range(2,int(i**0.5)+1):
                if i % j == 0:
                    cnt += 1
                    break
    return cnt
print(rootss(1,1000))