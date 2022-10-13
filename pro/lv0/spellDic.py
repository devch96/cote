def solution(spell, dic):
    answer = 2
    for i in dic:
        if set(spell) == set(i):
            answer = 1
    return answer
