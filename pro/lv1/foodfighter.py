def solution(food):
    answer = ''
    del food[0]
    for idx, cnt in enumerate(food):
        answer += str(idx+1)*(cnt//2)
    answer += '0'+answer[::-1]
    return answer
print(solution([1,3,4,6]))
print(solution([1,7,1,2]))