def solution(n):
    d = 2
    answer = []
    temp = []
    while d <= n:
        if n % d == 0:
            temp.append(d)
            n = n // d
        else:
            d+=1
    for i in set(temp):
        answer.append(i)
    answer.sort()
    return answer

"""
if n % d == 0:
    n /= d
    if d not in answer:
        answer.append(d)
"""
