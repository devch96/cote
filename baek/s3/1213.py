#팰린드롬 만들기
import sys
from collections import Counter
input = sys.stdin.readline
s = sorted(input().rstrip())
flag = True
c = Counter(s)
center = ""
cnt = 0
for i in c:
    if c[i] % 2 != 0:
        cnt += 1
        center += i
        s.remove(i)
    if cnt > 1:
        flag = False
        break
left = ""
for i in range(0,len(s),2):
    left += s[i]
print(left+center+left[::-1] if flag else "I'm Sorry Hansoo")