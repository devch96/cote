import sys
input = sys.stdin.readline
s = input().rstrip().split('-')
for i in range(len(s)):
    n = map(int, s[i].split('+'))
    s[i] = sum(n)
 
total = s[0]
for i in range(1, len(s)):
    total -= s[i]
print(total)