def solution(sides):
    if sum(sides) - max(sides) <= max(sides):
        answer = 2
    else:
        answer = 1
    return answer
