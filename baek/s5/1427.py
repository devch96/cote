#소트인사이드
import sys
input = sys.stdin.readline
s = input().rstrip()
print(''.join(sorted(s, reverse=True)))