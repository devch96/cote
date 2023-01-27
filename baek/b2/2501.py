#약수 구하기
import sys
input = sys.stdin.readline
n,k = map(int,input().split())
#6 , 3
measure = []
for i in range(1,(int(n**0.5)+1)):
    if n % i == 0:
        measure.append(i)
        if n//i != i:
            measure.append(n//i)
measure.sort()
if len(measure) >= k:
    print(measure[k-1])
else:
    print(0)