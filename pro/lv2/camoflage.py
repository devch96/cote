from collections import Counter
def solution(clothes):
    kinds = Counter(list(zip(*clothes))[1])
    answer = 1
    for i in kinds.values():
        answer *= (i+1)
    return answer-1 
