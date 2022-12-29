#귀걸이
import sys
from collections import Counter
input = sys.stdin.readline
no = 1
while True:
    t = int(input())
    if t == 0:
        break
    students = []
    earings = []
    for i in range(t):
        students.append(input().rstrip())
    for i in range((t*2)-1):
        a,b = map(str,input().split())
        earings.append(a)
    c = Counter(earings)
    for k,v in c.items():
        if v == 1:
            print(no, students[int(k)-1])
    no +=1 