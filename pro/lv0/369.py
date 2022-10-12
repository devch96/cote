def solution(order):
    answer = sum(map(str(order).count,['3','6','9']))
    return answer
