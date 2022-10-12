def solution(box,n):
    answer = 1
    for i in box:
        answer = answer * (i//n)
    return answer

"""
answer *= i // n
"""
