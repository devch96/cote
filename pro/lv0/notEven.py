def solution(n):
    answer = []
    for i in range(1,n+1):
        if i % 2 != 0:
            anwer.append(i)
    return answer

"""
n = (n+1) // 2
return [2*i+1 for i in range(n)]
"""
