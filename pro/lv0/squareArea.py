def solution(dots):
    answer = (max(dots)[0] - min(dots)[0]) * (max(dots)[1] - min(dots)[1])
    return answer
