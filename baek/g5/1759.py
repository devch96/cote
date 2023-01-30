#암호 만들기
import sys
from itertools import combinations
input = sys.stdin.readline
l,c = map(int,input().split())
letter = sorted(list(map(str,input().split())))
cons = [] # at least 2
vowel = [] # at least 1
for s in letter:
    if s in 'aeiou':
        vowel.append(s)
    else:
        cons.append(s)
pw = []
for c in list(combinations(letter, l)):
    vo_cnt = co_cnt = 0
    for char in c:
        if char in vowel:
            vo_cnt += 1
        else:
            co_cnt += 1
    if vo_cnt > 0 and co_cnt > 1:
        pw.append("".join(c))
for x in pw:
    print(x)
