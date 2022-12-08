import sys
input = sys.stdin.readline
t = int(input())
s = [0,1,3]
for i in range(3,1001):
    s.append(s[i-1] + (s[i-2])*2)
print(s[t] % 10007)