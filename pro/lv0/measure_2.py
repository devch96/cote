def solution(n):
    answer = 0
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            if i**2 == n:
                answer += 1
                continue
            answer += 2
    return answer
