import sys
input = sys.stdin.readline
n = int(input())
f = int(input())
tmp = (n//100)*100
while tmp%f != 0:
    tmp+=1
print(str(tmp)[-2:])