def solution(n):
    temp = 1
    answer = 0
    for i in range(n):
        i += 1
        temp*=i
        if temp==n:
            answer = i
            break
        elif temp > n :
            answer = i-1
            break
    return answer

"""
from math import factorial

k = 10
while n < factorial(k):
    k -= 1
return k
"""
