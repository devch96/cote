def solution(n):
    answer = 0
    for i in range(n):
        answer += 1
        while '3' in str(answer) or answer % 3 == 0:
            answer +=1
    return answer
