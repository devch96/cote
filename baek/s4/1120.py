#문자열
import sys
input = sys.stdin.readline
a,b = map(str,input().split())
answer = []
dif = len(b) - len(a)
for i in range(dif+1):
    cnt = 0
    for j in range(len(a)):
        if a[j] != b[i+j]:
            cnt +=1
    answer.append(cnt)
print(min(answer))