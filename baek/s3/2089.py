#-2진수
import sys
input = sys.stdin.readline
n = int(input())
def minusbin(x):
    if x == 0:
        return x
    result = ""
    while x:
        if x%-2:
            x = (x//-2) + 1
            result += '1'
        else:
            x = x//-2
            result += '0'
    return result[::-1]
print(minusbin(n))