#놀라운 문자열
import sys
input = sys.stdin.readline
while True:
    s = input().rstrip()
    if s == "*":
        break
    x = 1
    flag = True
    while x <= len(s)-2:
        temp = []
        for i in range(len(s)-x):
            temp.append(s[i] + s[i+x])
        if len(temp) != len(set(temp)):
            flag = False
        x+=1
    print(s+" is surprising." if flag else s+" is NOT surprising.")