def solution(array):
    answer = 0
    temp = list(map(str,array))
    for i in temp:
        answer += i.count('7')
    return answer
