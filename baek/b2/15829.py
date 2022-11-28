import sys
input = sys.stdin.readline
n = int(input())
str = input().strip()
def Hashing(s):
    result = 0
    for i in range(n):
        result += (ord(s[i])-96) * (31 ** i)
    return result % 1234567891
print(Hashing(str))