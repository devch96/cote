#진법 변환
import sys
input = sys.stdin.readline
table = dict()
for i in range(65,91):
    table[chr(i)] = i-55

x,y = input().split()
answer = 0
for i,s in enumerate(x[::-1]):
    if s in table:
        answer += table[s]* (int(y)**i)
    else:
        answer += int(s) * (int(y)**i)
print(answer)
