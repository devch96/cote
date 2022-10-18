def solution(n):
    measure =[]
    if n == 0:
        return 0
    for i in range(1,int(n**0.5)+1):
        if n % i == :
            measure.append(i)
            if i != n//i:
                measure.append(n//i)
    answer = sum(measure)
    return answer

