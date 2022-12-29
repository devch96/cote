#폴리오미노
import sys
input = sys.stdin.readline
s = input().rstrip()
s = s.replace("XXXX","AAAA")
s = s.replace("XX","BB")
if s.count("X"):
    print(-1)
else:
    print(s)