def solution(hp):
    first = hp // 5
    hp = hp - first*5
    second = hp // 3
    hp = hp - second*3
    third = hp // 1
    answer = first + second + third
    return answer

"""
answer = 0
for ant in [5,3,1]:
    d, hp = divmod(hp,ant)
    answer += d
return answer
"""
